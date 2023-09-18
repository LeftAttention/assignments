import argparse
import re
from collections import Counter

def parse_args():
    parser = argparse.ArgumentParser(description='Count the occurrences of each word in a text file.')
    parser.add_argument('--file_path', help='Path to the text file')

    return parser.parse_args()

def main():

    args = parse_args()

    try:
        with open(args.file_path, 'r', encoding='utf-8') as f:

            text = f.read()
            words = re.findall(r'\b\w+\b', text, re.IGNORECASE)

            word_counts = Counter(word.lower() for word in words)

            for word, count in word_counts.items():
                print(f'{word}: {count}')

    except FileNotFoundError:
        print(f'File not found: {args.file_path}')

if __name__ == "__main__":
    main()