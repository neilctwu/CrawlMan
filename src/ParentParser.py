from src.HttpGetter import HttpGetter
from src.utils.tools import random_sleep

from bs4 import BeautifulSoup


class ParentParser(HttpGetter):
    def __init__(self, url, subpage, selectors, logger):
        self.page_list = []
        self.url_list = []
        self.selectors = selectors
        url = url+subpage
        page = ''
        end = False
        while not end:
            super(ParentParser, self).__init__(url+page)
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            self._parse_url()
            # Loggingup
            logger.log_parent(self.url_list)
            # To next page
            page = self._next_page()
            random_sleep(15, 30)
            if page is None:
                end = True

    def _parse_url(self):
        elems = self.soup.select(self.selectors['url'])
        for elem in elems:
            url = elem.get('href')
            if url in self.url_list:
                continue
            self.url_list.append(elem.get('href'))

    def _next_page(self):
        elems = self.soup.select(self.selectors['page'])
        pages = [elem.get('href').split('/')[-1] for elem in elems]
        for page in pages:
            if page in self.page_list:
                continue
            else:
                self.page_list.append(page)
                return page
        return None
