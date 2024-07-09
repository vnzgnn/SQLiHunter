# SQLiHunter

**SQLiHunter** is a SQL Injection (SQLi) vulnerability scanner written in Python. It leverages the Wayback Machine to gather URLs with parameters from the target site and tests a series of SQLi payloads to detect potential vulnerabilities.

## Features

- Collect URLs with parameters from the target site using the Wayback Machine.
- Generate common SQLi payloads to test for vulnerabilities.
- Double-check results with benign queries to reduce false positives.
- Real-time output of found SQLi vulnerabilities.

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
