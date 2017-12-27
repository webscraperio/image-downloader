# Image Downloader

Image downloader script finds image urls scraped by Image Selector in a csv file and downloads them.
Images are renamed to `<web-scraper-oder>-<selector-name>.ext`.

### Windows usage

1. Download and install python 3.x from here:
[https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download image downloader script from here:
[https://github.com/webscraperio/image-downloader][image-downloader]
3. Scrape the target site and export data in CSV format
4. Drag and drop the CSV file on top of the `image-downloader.py`
![Fig. 1: windows image download][windows-image-download-script]

### macOS, Linux usage

1. Install python if necessary through your package manager. Most likely you already have it preinstalled.
2. Download image downloader script from here:
[https://github.com/webscraperio/image-downloader][image-downloader]
3. Move `image-downloader.py` to `Downloads` directory
4. Scrape the target site and export data in CSV format
5. Save the CSV file in `Downloads` directory
6. Open `Terminal` application. You should have one preinstalled
7. Change working to `Downloads` directory by typing:
    ```bash
    cd Downloads
    ```
8. Run image downloader script by typing:
    ````bash
    python image-downloader scraped_data.csv
    ````

![Fig. 2: macOS image download][osx-image-download-script]

 [windows-image-download-script]: docs/images/win-image-downloader.gif?raw=true
 [osx-image-download-script]: docs/images/osx-image-downloader.gif?raw=true
 [image-downloader]: https://github.com/webscraperio/image-downloader/releases
 