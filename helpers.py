from abc import ABC, abstractmethod

class StatusCodeIssue(Exception):
    def __int__(self, arg):
        self.msg = arg

class FetchIssue(Exception):
    def __int__(self, arg):
        self.msg = arg



class ISWebscrape(ABC):

    @abstractmethod
    def fetch_page(self):
        pass

    @abstractmethod
    def get_soup(self):
        pass

  
