from src.HttpGetter import HttpGetter
from dic.stopwords import stopwords
from src.utils.tools import hashhex

from bs4 import BeautifulSoup
import pickle
import os


class ChildParser(HttpGetter):
    def __init__(self, url, selectors, output_dir='./output/', summary=False):
        super(ChildParser, self).__init__(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.selectors = selectors
        self.output_dir = output_dir
        self.data = {}
        self._parse_all()
        if summary:
            self._parse_sum()
        self._cleaning_all()
        self._save()

    def _parse_all(self):
        self.data['url'] = self.url
        self._parse_text('name')
        self._parse_text('time')
        self._parse_text('body')

    def _parse_sum(self):
        sums = self.soup.select(self.selectors['summary'])
        if not sums:
            self.data['summary'] = ''
        sums = [x.text for x in sums]
        self.data['summary'] = '<sep>'.join(sums)

    def _parse_text(self, tag):
        elem = self.soup.select_one(self.selectors[tag])
        self.data[tag] = elem.text if elem is not None else ''

    def _cleaning_all(self):
        for key in self.data:
            self.data[key] = self._cleaning(key)

    def _cleaning(self, key):
        text = self.data[key]
        for word in stopwords:
            text = text.replace(word, '')
        text = text.rstrip(' ').lstrip(' ')
        return text

    def _save(self):
        hexname = hashhex(self.url)
        # Check directory
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        with open('{}/{}.pickle'.format(self.output_dir, hexname), 'wb') as f:
            pickle.dump(self.data, f)
