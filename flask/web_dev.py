import requests
from bs4 import BeautifulSoup
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Web Scraping from an URL')
    parser.add_argument('--url', help='URL', default="https://www.bbc.com/news")

    return parser.parse_args()

def main():

    args = parse_args()

    try:
        response = requests.get(args.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = soup.find_all('div')
        
        for i, item in enumerate(data):
            class_name = item.get('class')
            print(f"\nItem {i+1}:")
            print(f"   Text: {item.get_text()}")
            print(f"   Tag Name: {item.name}")
            print(f"   Class Name: {' '.join(class_name) if class_name else 'No Class'}")


    except Exception as e:
        print(f"There is an error :\n{e}")

if __name__ == "__main__":
    main()