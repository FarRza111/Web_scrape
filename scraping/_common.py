import requests
from bs4 import BeautifulSoup
import typing as ty
import requests



# url = 'https://cv.ee/en/search?limit=20&offset=0&fuzzy=true&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=false&isQuickApply=false'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def fetch_page(url:str, headers: ty.Dict[str, ty.Any])-> ty.Union[requests.Response, str]:
    try:
        return requests.get(url = url, headers= headers)
    except requests.RequestException as e:
        return {'status': 500, 'message': f'error occured {e}'}
    return None


def form_soup(response: requests.Response, parser: ty.Literal["html.parser", "lxml"] = "html.parser"):
    return BeautifulSoup(response.content, parser)

if __name__ == "__main__":

    for i in range(10):
        url = f'https://bina.az/baki/alqi-satqi/menziller?page={i}'
    page = fetch_page(url, headers)
    soup = form_soup(page)
    print(soup)

