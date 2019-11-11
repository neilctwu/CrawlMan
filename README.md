# CrawlMan
News crawler for NLP data preparation

## Super short introduction
---
**ParentParser** for url list crawling
**ChildParser** for url content crawling

## Input features
```
url = 'https://example.com/'  # <Pseudo url, for saving
subpage = 'folder/some'  # List url, ParentParser crawling from https://example.com/folder/some

features = {'extent_link': False, 'summary_exist': True, 'summary_samepage': True}

# Css selectors for contents
selectors = {'parent': {'url': 'ul.article>li>a',
                        'page': 'ul.page>li>a'},
             'child': {'name': 'h1.Ttl',
                       'time': 'time.Time',
                       'body': 'div.Body"]',
                       'summary': 'ul.summary'}}

# If url from parentparser not equal to url for childparser
def url_changer(x):
    return x.replace('a', 'b')
```
