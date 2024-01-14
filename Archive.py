from bs4 import BeautifulSoup
from colorama import Fore
import requests

class ArchiveDownloader:
    def __init__(self):
        self.archive_urls = {}

    def get_archive_urls(self, url):
        """
        Retrieves archive URLs from the provided URL.

        Args:
            url (str): The URL to scrape for archive URLs.

        Returns:
            dict: Dictionary of archive names and URLs.
        """
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails

        html_content = response.content

        # Parse the HTML code
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all <a> elements with a specific class or attribute that identifies archive links
        archive_links = soup.find_all('a', class_='archive-link')

        # Extract the archive URLs and names
        self.archive_urls = {}
        for link in archive_links:
            href = link['href']
            name = link.text.strip()
            if href is not None and name is not None and href.endswith('.zip'):
                self.archive_urls[name] = href

        return self.archive_urls

    def download_archive(self, url, filename):
        """
        Downloads the archive file from the provided URL.

        Args:
            url (str): The URL of the archive file to download.
            filename (str): The desired filename for the downloaded file.
        """
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception if the request fails
        print(f"{Fore.YELLOW}Downloading Archive: {filename}")
        print(f"{Fore.YELLOW}With URL: {url}\n")
        with open(filename + ".zip", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
