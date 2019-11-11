import os
import pdb


class Logger:
    def __init__(self, site_name, path='log'):
        self.log_path = '{}/{}/'.format(path, site_name)
        self._check_path(self.log_path)

        with open(self.log_path+'log_url_finished.txt', 'r') as f:
            self.list_crawled = f.readlines()
            self.list_crawled = [x.rstrip('\n') for x in self.list_crawled]
        self.file_crawled = open(self.log_path+'log_url_finished.txt', 'a')

        with open('log/news.livedoor.com/log_url_parent.txt', 'r') as f:
            self.list_url = f.readlines()
            self.list_url = [url.rstrip('\n') for url in self.list_url]
        self.file_url = open(self.log_path+'log_url_parent.txt', 'a')

    @staticmethod
    def _check_path(log_path):
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        if not os.path.exists(log_path+'log_url_finished.txt'):
            open(log_path+'log_url_finished.txt', 'a').close()
        if not os.path.exists(log_path+'log_url_parent.txt'):
            open(log_path+'log_url_parent.txt', 'a').close()

    def log_parent(self, url_list):
        # pdb.set_trace()
        url_prune = [x for x in url_list if not self.check_url(x, self.list_url, child=False)]
        for url in url_prune:
            self.file_url.write(url+'\n')
            self.list_url.append(url)
        self.file_url.close()
        self.file_url = open(self.log_path + 'log_url_parent.txt', 'a')

    def log(self, url):
        """
        logging url
        :param url:
        :return:
        """
        self.file_crawled.write(url+'\n')
        self.file_crawled.close()
        self.file_crawled = open(self.log_path + 'log_url_finished.txt', 'a')
        self.list_crawled.append(url)

    def check_url(self, url, url_list=None, child=True):
        if child:
            if url in self.list_crawled:
                return True
            else:
                return False
        else:
            if url in url_list:
                return True
            else:
                return False
