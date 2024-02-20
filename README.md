# Bind-SQL-Detector
Tool for detecting time-based SQL injections
# SQL Injection Time-Based Detector

This is a Python script that detects potential time-based SQL injections in a web application. The tool sends HTTP requests with different payloads and analyzes the response time to determine potential vulnerabilities.

## Installation

1. Clone this repository to your local machine:

2. Navigate to the repository directory:
cd sqli-detector
3. Install the necessary dependencies using pip:
pip install -r requirements.txt

## Usage

Run the `sqli.py` script providing the URL of the web application you want to test and any necessary parameters.
python3 sqli.py <URL> [options]

### Parameters Syntax

- `--get`: Specify the GET parameters as key-value pairs separated by spaces. Example: `--get "key1=value1" "key2=value2"`
- `--post`: Specify the POST parameters as key-value pairs separated by spaces. Example: `--post "key1=value1" "key2=value2"`
- `--cookie`: Specify the cookies as key-value pairs separated by spaces. Example: `--cookie "key1=value1" "key2=value2"`
- `--proxy`: Specify the proxy address for sending requests. Example: `--proxy "http://127.0.0.1:8080"`
- `--payload-file`: Specify the file containing the SQL injection payloads. By default, `payloads.txt` is used.

### Example Usage
python3 sqli.py "http://example.com/login" --get "username=admin" "password=pass123" --cookie "sessionid=abc123" --proxy "http://127.0.0.1:8080"
![2024-02-20 13_21_47-kali-linux-2023 4-vmware-amd64 - VMware Workstation](https://github.com/marcocarolasec/Bind-SQL-Detector/assets/58811847/22c23ca8-a71c-4012-b753-3a85afc528b0)


## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## Acknowledgments

This project was inspired by the need to enhance security in web applications.

## License

This project is licensed under the Open Source License by MarcoCarolaSec.









