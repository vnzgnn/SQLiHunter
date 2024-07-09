# SQLiHunter

**SQLiHunter** is a powerful and efficient SQL Injection (SQLi) vulnerability scanner written in Python. Designed for security researchers and penetration testers, SQLiHunter leverages the extensive archive of the Wayback Machine to collect URLs with parameters from the target website. It then systematically tests these URLs with a series of common SQLi payloads to detect potential vulnerabilities.

SQLiHunter aims to provide a thorough and reliable assessment of a website's security posture against SQL injection attacks. By using both common and custom SQLi payloads, it can identify vulnerabilities that might be exploited by malicious attackers to gain unauthorized access to a database or manipulate its contents.

The tool incorporates a double-check mechanism that compares the results with benign queries to reduce false positives, ensuring that the reported vulnerabilities are accurate and relevant. SQLiHunter offers real-time reporting of identified vulnerabilities, allowing security professionals to take immediate action to mitigate any risks.

Key features include:

- **Automated URL Collection**: Utilizes the Wayback Machine to gather a comprehensive list of URLs with parameters from the target site, providing a robust base for testing.
- **Payload Generation**: Creates a variety of SQLi payloads to test for different types of SQL injection vulnerabilities.
- **Real-time Detection**: Outputs potential vulnerabilities in real-time as they are discovered, enabling quick response and remediation.
- **False Positive Reduction**: Implements a benign query verification step to minimize false positives and ensure the accuracy of the results.
- **User-friendly**: Simple command-line interface for ease of use, making it accessible for both beginners and experienced security professionals.

## Requirements

- Python 3.7+
- Python libraries: `requests`, `httpx`, `argparse`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/SQLiHunter.git
    cd SQLiHunter
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## How It Works

1. Run the program with the command:

    ```bash
    python3 SQLiHunter.py -u http://example.com/
    ```

    Replace `http://example.com/` with the actual target URL you want to analyze.

2. The program will collect URLs from the target site using the Wayback Machine and generate SQLi payloads to test for vulnerabilities.

3. The results of found vulnerabilities will be displayed in real-time.

## Usage Example

```bash
python3 SQLiHunter.py -u http://www.example.com/
```

## Contributing

Contributions are welcome! Feel free to open issues or make pull requests with improvements and fixes.

## Disclaimer

This tool is intended for research and penetration testing purposes only. Use of this tool for illegal activities is strictly prohibited. The author is not responsible for any misuse or damage caused by this tool.
