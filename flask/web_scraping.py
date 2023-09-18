import requests
from bs4 import BeautifulSoup
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Web Scraping from an URL')
    parser.add_argument('--url', help='URL', default="https://medium.com/")

    return parser.parse_args()

def main():

    args = parse_args()

    try:
        response = requests.get(args.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('title')
        print(f'The title of the webpage is: {title.string}')
    except Exception as e:
        print(f"There is an error :\n{e}")


if __name__ == "__main__":
    main()