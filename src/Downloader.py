import argparse
from bs4 import BeautifulSoup

import requests


parser = argparse.ArgumentParser(description="Downloads all video files in the given page")

parser.add_argument('-l', '--Link', help='Page Url', required=True)
parser.add_argument("-o", "--Output", help="Output directory")

args = parser.parse_args()
url = args.Link
