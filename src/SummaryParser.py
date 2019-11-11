from src.HttpGetter import HttpGetter

from bs4 import BeautifulSoup


class SummaryParser:
    def __init__(self, url_changer, sum_selector):
        self.url_changer = url_changer
        self.selectors = sum_selector

    def __call__(self, url):
        url = self.url_changer(url)
        httpgetter = HttpGetter(url)
        self.soup = BeautifulSoup(httpgetter.response.text, 'html.parser')
        summaries = self._parse_sum()
        return summaries

    def _parse_sum(self):
        sums = self.soup.select(self.selectors)
        if not sums:
            return ''
        sums = [x.text for x in sums]
        return '<sep>'.join(sums)
