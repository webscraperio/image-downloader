#! /usr/bin/env python3

import csv
import shutil
import sys
import time
import os
import logging

# http client configuration
# Chrome version on Windows 10 64-bit (as of end Aug 2023)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

# logging configuration
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# delay in seconds, fraction of a second is OK
dl_delay = 0.25

python_version = sys.version_info.major
logging.info("executed by python %d" % python_version)

# Ended support for Python 2
if python_version == 3:
    import urllib.parse
    import urllib.request
    urljoin = urllib.parse.urljoin
    urlretrieve = urllib.request.urlretrieve
    quote = urllib.parse.quote

    # configure headers
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    urllib.request.install_opener(opener)
else:
    print("Python 2 is not supported. Please use Python 3.")
    print("Exiting the program...")
    sys.exit(1)

    # configure headers
    class AppURLopener(urllib.FancyURLopener):
        version = user_agent
    urllib._urlopener = AppURLopener()

def fix_url(url):
    url = quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    return url


def download_csv_row_images(row, dest_dir):
    for key in row:
        start_url = row['web-scraper-start-url']
        id = row['web-scraper-order']

        if key.endswith("-src"):
            image_url = row[key]
            image_url = urljoin(start_url, image_url)

            image_filename = "%s-%s" % (id, key[0:-4])
            download_image(image_url, dest_dir, image_filename)


def download_image(image_url, dest_dir, image_filename):

    image_url = fix_url(image_url)

    try:
        logging.info("downloading image %s" % image_url)
        tmp_file_name, headers = urlretrieve(image_url)
        content_type = headers.get("Content-Type")

        if content_type == 'image/jpeg' or content_type == 'image/jpg':
            ext = 'jpg'
        elif content_type == 'image/png':
            ext = 'png'
        elif content_type == 'image/gif':
            ext = 'gif'
        elif content_type == 'image/webp':
            ext = 'webp'
        else:
            logging.warning("unknown image content type %s" % content_type)
            return

        image_path = os.path.join(dest_dir, image_filename+"."+ext)
        shutil.move(tmp_file_name, image_path)
    except Exception as e:
        logging.warning("Image download error. %s" % e)

def get_csv_image_dir(csv_filename):

    base = os.path.basename(csv_filename)
    dir = os.path.splitext(base)[0]

    if not os.path.exists(dir):
        os.makedirs(dir)

    return dir

def download_csv_file_images(filename):

    logging.info("importing data from %s" % filename)

    dest_dir = get_csv_image_dir(filename)

    #check whether csv file has utf-8 bom char at the beginning
    skip_utf8_seek = 0
    with open(filename, "rb") as csvfile:
        csv_start = csvfile.read(3)
        if csv_start == b'\xef\xbb\xbf':
            skip_utf8_seek = 3


    with open(filename, "r", encoding="utf8") as csvfile:

        # remove ut-8 bon sig
        csvfile.seek(skip_utf8_seek)

        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            download_csv_row_images(row, dest_dir)
            # delay in seconds. Disable line below for no delay.
            time.sleep(dl_delay)

def main(args):

    # filename passed through args
    if len(args) >=2:
        csv_filename = args[1]
        download_csv_file_images(csv_filename)
        logging.info("image download completed")

    else:
        logging.warning("no input file found")

    # Removed the 10-second delay and replaced it with call to Windows' built-in Pause
    # Enable the os.system line when creating app file with PyInstaller
    # This only works for Windows .exe
    # It will display "Press any key to continue..."
    os.system('pause') 

    # Restore the line below and disable the os.system line if you want 10-second delay 
    # after downloading is done
    # time.sleep(10)

main(sys.argv)
