# 🎧 Archive Downloader

> A Python script to download archive files from the provided URLs.

## ⚙ Installation :
```bash
pip install beautifulsoup4
pip install colorama
pip install requests
```

## ❓ Usage :
```python
from archive_downloader import ArchiveDownloader

# Create an instance of ArchiveDownloader
downloader = ArchiveDownloader()

"""Add target URLs here"""
urls = [""]

for url in urls:
    # Get the archive URLs from the provided URL
    result = downloader.get_archive_urls(url)

    for archive_name, archive_url in result.items():
        # Download the archive file
        downloader.download_archive(archive_url, archive_name)
```
## 🪐 Credits:
* [Dexter](https://github.com/dexter-90) For [Archive-Scraper](https://github.com/dexter-90/Archive-Scraper)
