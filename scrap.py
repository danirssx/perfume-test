import pandas as pd
import numpy as np
import bs4 as BeautifulSoup
import requests
import time


class Script:

    # Link to scrap main excel data
    def link_excel(self, link):
        df = pd.DataFrame(columns='Perfumes')
        df['Perfumes'] = pd.read_excel(link)

        return df

    # Tool to scrape the website
    def scrap_tool(self, url):
        delay_seconds = 2
        time.sleep(delay_seconds)

        # Where I'm accessing to the data
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'DNT': '1',  # "Do Not Track" header
            'Referer': 'https://www.google.com',  # Simulate coming from a search engine
        }

        # Request access to website
        session = requests.Session()
        response = session.get(url, headers=headers)

        # Transforming it into soup
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup
