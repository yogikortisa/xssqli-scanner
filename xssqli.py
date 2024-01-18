import requests

def check_xss(url):
    # Function to check for XSS vulnerabilities
    # XSS payloads to be tested
    payloads = ['<script>alert("XSS")</script>', '<img src="x" onerror="alert(\'XSS\')">', '"><script>alert("XSS")</script>']
    
    for payload in payloads:
        test_url = f"{url}{payload}"
        response = requests.get(test_url)
        
        # Check if the payload is present in the response content
        if payload in response.text:
            print(f"XSS Vulnerability found in {url}")
            return True
    
    print(f"No XSS Vulnerability found in {url}")
    return False

def check_sql_injection(url):
    # Function to check for SQL Injection vulnerabilities
    # SQL injection payloads to be tested
    payloads = ["'", "\""]
    
    for payload in payloads:
        test_url = f"{url}{payload}"
        response = requests.get(test_url)
        
        # Common error messages indicating a potential SQL Injection vulnerability
        errors = {
            "you have an error in your sql syntax;",
            "warning: mysql",
            "unclosed quotation mark after the character string",
            "quoted string not properly terminated",
        }
        
        # Check if any of the predefined error messages is present in the response content
        for error in errors:
            if error in response.content.decode().lower():
                print(f"SQL Injection Vulnerability found in {url}")
                return True
    
    print(f"No SQL Injection Vulnerability found in {url}")
    return False

def main():
    # Main function to take user input and perform security checks
    web_app_url = input("Enter the web application URL and GET Parameter (Example: https://example.com?parameter=value): ")
    
    # Perform XSS and SQL Injection checks
    xss_result = check_xss(web_app_url)
    sql_injection_result = check_sql_injection(web_app_url)
    
    # Print a summary based on the results
    if not xss_result and not sql_injection_result:
        print("No common web application security vulnerabilities found.")

if __name__ == "__main__":
    main()
