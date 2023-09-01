# Image Downloader

Image downloader script finds image URLSs previously scraped by Image Selector in a csv file and downloads them. Images are renamed to `<web-scraper-order>-<selector-name>.ext`. This version is a fork from webscraper.io's original at [https://github.com/webscraperio/image-downloader]. I have made some small tweaks:

- A Windows binary (.Exe) is available for those who cannot, or will not install Python.
- Changed the User-agent to the one for the latest Chrome on Windows 10 64-bit. The original script is reporting itself as "Chromium 63 on Ubuntu".
- Removed the 10-second delay when downloads are completed, and replaced it with a call to Windows' built-in Pause command. This will display "Press any key to continue..." instead of closing the console window after 10 seconds.
- Added a 0.25 second delay between each download. You can change or remove this in the source.
- A sample scrape results file, `sample-images-dl.csv` is available to testing. Ypu cam drag-n-drop this file on the .EXE or .py file for testing.

### Windows usage

1. \[OPTIONAL\] Download and install python 3.x from here:
[https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download image downloader .EXE and script from here:
[https://github.com/LeeMeng2020/image-downloader/releases][image-downloader-releases]
3. Scrape the target site and export data in CSV format
4. Drag and drop the CSV file onto `image-downloader.exe`
![Fig. 1: Windows image download][windows-exe-drag-n-drop]
5. Alternatively, if you have Python 3.x installed, drag and drop the CSV file onto `image-downloader.py`. On some computers, you may need to [enable drag & drop onto Python files](https://youtu.be/JrksuHFYrRE).

### MacOS, Linux usage

1. Install python if necessary through your package manager. Most likely you already have it preinstalled.
2. Download image downloader script from here:
[https://github.com/LeeMeng2020/image-downloader][image-downloader]
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

 [windows-exe-drag-n-drop]: docs/images/win-drag-n-drop.png
 [windows-image-download-script]: docs/images/win-image-downloader.gif?raw=true
 [osx-image-download-script]: docs/images/osx-image-downloader.gif?raw=true
 [image-downloader-releases]: https://github.com/LeeMeng2020/image-downloader/releases
 [image-downloader]: https://github.com/LeeMeng2020/image-downloader
 