# Graded Assignment on Networking and Servers

## Installation

```bash
pip install requests prettytable
```

## Explanation

This script is designed to monitor the status of various subdomains, determining whether they are accessible (up) or not (down). It prints the results in a tabular format in the console.

## Functionality
- The script sends HTTP GET requests to each subdomain.
- If a response is received, the script checks the HTTP status code to determine if the subdomain is 'Up' or 'Down'.
- If there is a connection error, timeout, or any other request exception, the subdomain is marked as 'Down'.
- It prints out the status of each subdomain every minute in a table with columns: 'Subdomain', 'Status Code', and 'Status'.
