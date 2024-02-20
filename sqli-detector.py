import requests
import argparse
import time
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Colores para el texto
COLOR_SUCCESS = Fore.GREEN
COLOR_ERROR = Fore.RED
COLOR_INFO = Fore.CYAN

def check_sqli_time_based(url, method, params, cookies, proxy, payload_file):
    with open(payload_file, 'r') as f:
        payloads = f.readlines()

    for param_name, param_value in params.items():
        for payload in payloads:
            payload = payload.strip()
            params[param_name] = payload
            try:
                start_time = time.time()
                if method == 'GET':
                    response = requests.get(url, params=params, cookies=cookies, proxies=proxy)
                elif method == 'POST':
                    response = requests.post(url, data=params, cookies=cookies, proxies=proxy)
                else:
                    print(f"{COLOR_ERROR}[-] Invalid HTTP method specified.")
                    return
                
                end_time = time.time()
                response_time = end_time - start_time

                if response_time >= 20:
                    print(f"{COLOR_SUCCESS}[+] Possible SQL injection found with payload:")
                    print(f"{COLOR_INFO}    URL: {url}")
                    print(f"{COLOR_INFO}    Parameter: {param_name}={payload}")
                    print(f"{COLOR_INFO}    Response Time: {response_time:.2f} seconds")
            except Exception as e:
                print(f"{COLOR_ERROR}[-] Error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='SQL Injection Time-Based Detector')
    parser.add_argument('url', type=str, help='URL to test for SQL injection')
    parser.add_argument('--get', type=str, help='GET parameters as key value pairs', nargs='+', default={})
    parser.add_argument('--post', type=str, help='POST parameters as key value pairs', nargs='+', default={})
    parser.add_argument('--cookie', type=str, help='Cookies as key value pairs', nargs='+', default={})
    parser.add_argument('--proxy', type=str, help='Proxy address for sending requests', default=None)
    parser.add_argument('--payload-file', type=str, help='File containing SQL injection payloads', default='payloads.txt')

    args = parser.parse_args()

    url = args.url
    params = {}
    cookies = {}
    proxy = None

    if args.get:
        method = 'GET'
        for param in args.get:
            key, value = param.split('=')
            params[key] = value
    elif args.post:
        method = 'POST'
        for param in args.post:
            key, value = param.split('=')
            params[key] = value

    for cookie in args.cookie:
        key, value = cookie.split('=')
        cookies[key] = value

    if args.proxy:
        proxy = {'http': args.proxy, 'https': args.proxy}

    check_sqli_time_based(url, method, params, cookies, proxy, args.payload_file)

if __name__ == "__main__":
    main()
