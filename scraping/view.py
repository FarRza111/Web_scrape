from scraping.implement import *
from scraping.implement._abc import *
from collections import defaultdict
from _common import *
import pandas as pd


class ISWebscrape(ISABC):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_soup(self):
        response = fetch_page(self.url, self.headers)
        if response.status_code == 200:
            return form_soup(response, 'html.parser')
        return None

    def scrape(self, soup):
        container = defaultdict(list)

        items = soup.select('div.card_params')
        for i in items:
            if i is None:
                continue

            price = i.select_one('.price-val').text,
            currency = i.select_one('.price-cur').text,
            location = i.select_one('.location').text,
            room_size = [li.text for li in i.select('ul.name li')][0],
            date = i.select_one('.city_when').text.split(',')[1],
            city = i.select_one('.city_when').text.split(',')[0]

            container["city"].append(city)
            container['date'].append(date)
            container['price'].append(price)
            container['location'].append(location)
            container['currency'].append(currency)
            container['room_size'].append(room_size[0])

        return pd.DataFrame(container)

    def process_soup(self):
        pass


if __name__ == "__main__":
    base_url = "https://bina.az/baki/alqi-satqi/menziller?page="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    all_data = pd.DataFrame()

    for i in range(1, 10):
        url = base_url + str(i)
        iswebscrape = ISWebscrape(url, headers)
        soup_pool = iswebscrape.get_soup()
        scrape = iswebscrape.scrape(soup_pool)
        all_data = pd.concat([all_data, scrape], ignore_index=True)

    all_data.to_excel('mdata.xlsx', index=False)
    print("Excel file exported successfully.")
