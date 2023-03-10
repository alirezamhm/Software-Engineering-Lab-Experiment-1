import argparse
from bs4 import BeautifulSoup
import requests

FORMATS = ('.mkv', '.mp4')

parser = argparse.ArgumentParser(description="Downloads all video files in the given page")

parser.add_argument('-l', '--Link', help='Page Url', required=True)
parser.add_argument("-o", "--Output", help="Output directory for downloads", required=True)

args = parser.parse_args()
url = args.Link
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

url = url[:url.index("?")] if "?" in url else url

video_hrefs = []
for link in soup.find_all('a'):
    href = link.get('href')
    if not href:
        continue
    if href.endswith(FORMATS):
        video_hrefs.append(href)
        
print(f"Number of videos found: {len(video_hrefs)}")
