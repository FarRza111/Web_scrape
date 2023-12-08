import pandas as pd
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import requests
import typing as ty
from typing import Union
from abc import ABC, abstractmethod
from helpers import *
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Item:
    city: str
    date: str
    price: int
    location: str
    currency: int
    room_size: Optional[str] = None
    # def __post_init__(self):
    #     if isinstance(self.price, str):
    #         raise TypeError('string is not a valid attribute type for price')
    #     if isinstance(self.currency, str):
    #         raise TypeError(f'string is not a valid attribute type for currency')
    #     else:
    #         ...

class WebScraper(ISWebscrape):

    def __init__(self, url: str, headers: ty.Dict[str, ty.Any]):
        self.url = url
        self.headers = headers
        self.list_of_items = []  # when is necessary to collect items into the list

    def fetch_page(self):
        try:
            return requests.get(url=self.url, headers=self.headers)
        except requests.RequestException as e:
            return f'THIS IS THE ERROR MESSAGE: {e} and {requests.Response}'

    def get_soup(self):
        page = self.fetch_page()
        status_code = page.status_code
        if page and status_code == 200:
            soup = BeautifulSoup(page.text, 'html.parser')
            return soup
        else:
            return None

    def get_data(self) -> pd.DataFrame:
        container = defaultdict(list)

        items = self.get_soup().select('div.card_params')
        for i in items:
            if i is None:
                continue

            # container["city"].append(city)
            # container['date'].append(date)
            # container['price'].append(price_value)
            # container['location'].append(location)
            # container['currency'].append(price_currency)
            # container['room_size'].append(room_info[0])

            DATA = Item(
                price=i.select_one('.price-val').text,
                currency=i.select_one('.price-cur').text,
                location=i.select_one('.location').text,
                room_size=[li.text for li in i.select('ul.name li')][0],
                date=i.select_one('.city_when').text.split(',')[1],
                city=i.select_one('.city_when').text.split(',')[0]
            )

            self.list_of_items.append(DATA)

        return pd.DataFrame(self.list_of_items)

    def save_to_excel(self):
        final_data = self.get_data()
        return final_data.to_excel('mydata.xlsx')


if __name__ == "__main__":
    url = "https://bina.az"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    cs = WebScraper(url, headers)
    # print(cs.get_soup())
    # print(cs.fetch_page())
    # print(cs.get_soup())
    print(cs.get_data())

    # print(cs.save_to_excel())
