import argparse
import os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import progressbar
import requests

FORMATS = ('.mkv', '.mp4')

parser = argparse.ArgumentParser(description="Downloads all video files in the given page")

parser.add_argument('-l', '--Link', help='Page Url', required=True)
parser.add_argument("-o", "--Output", help="Output directory for downloads")

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

pbar =  None
def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()
    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

output_dir = args.Output if args.Output else "./local"
os.makedirs(output_dir, exist_ok=True)
for href in video_hrefs:
    print(f"Downloading: {href}")
    try:
        if href.startswith("http"):
            video_url = href
        else:
            video_url = url + href
        file_name = href.split("/")[-1].replace("%20", " ")
        urlretrieve(video_url.replace(" ", "%20"), os.path.join(output_dir, file_name), show_progress)
    except Exception as e:
        print(f"Exception occured \n{e}")
print("Download finished.")