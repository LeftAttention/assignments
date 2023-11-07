import requests
from prettytable import PrettyTable
from time import sleep
from datetime import datetime

SUBDOMAINS = [
    'https://www.isro.gov.in/missionsupport.html',  # Real
    'https://www.isro.gov.in/GroundSystemSupport.html', # Real
    'https://www.isro.gov.in/UNNATI.html',  # Real
    'https://www.isro.gov.in/Visitors.html',    # Real
    'https://www.isro.gov.in/VedaServices.html',    # Fake
    'https://www.isro.gov.in/MobileApp.html',   # Fake
]

def check_subdomains(subdomains):
    table = PrettyTable(['Time', 'Subdomain', 'Status Code', 'Status'])

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=5)
            status_code = response.status_code
            if response.ok:
                status = 'Up'
            else:
                status = 'Down'
        except requests.ConnectionError:
            status_code = 'N/A'
            status = 'Down'
        except requests.Timeout:
            status_code = 'N/A'
            status = 'Timeout'
        except requests.RequestException as e:
            status_code = 'N/A'
            status = 'Error'
        
        table.add_row([current_time, subdomain, status_code, status])
    
    return table

def main():
    while True:
        table = check_subdomains(SUBDOMAINS)
        print(table)
        sleep(60)  # Wait for 1 minute

if __name__ == "__main__":
    main()