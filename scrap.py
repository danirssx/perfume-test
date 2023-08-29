import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time


class Script:

    # Link to scrap main excel data
    def link_excel(self, link):
        df = pd.DataFrame(columns=['Perfumes'])
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

        print('Response:', response.status_code)

        # Transforming it into sosup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Transforming the image
        image = soup.find('img', attrs={"width": "375"})
        img_src = image['src']

        # Transforming text
        text = soup.find('div', attrs={'itemprop': 'description'})
        paragraph = text.find('p', attrs={})
        p_text = paragraph.get_text()

        list_panda = [img_src, p_text]

        return list_panda

# Return prop

# TESTING

# data = Script()
# scrap = data.scrap_tool(
#     'https://www.fragrantica.es/perfume/Victoria-s-Secret/Victoria-s-Secret-Pink-Warm-Cozy-20400.html')


# print(scrap)
