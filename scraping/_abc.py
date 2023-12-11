import abc
from abc import abstractmethod, ABC

class ISABC(abc.ABC):

    @abstractmethod
    def get_soup(self):
        pass

    @abstractmethod
    def process_soup(self):
        pass

    @abstractmethod
    def scrape(self):
        pass


