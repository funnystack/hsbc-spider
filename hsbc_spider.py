# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import requests
import bs4

class ExchangeRateSpider(object):
    def craw(self):
        html_cont = self.download('https://www.services.cn-banking.hsbc.com.cn/PublicContent/common/rate/zh/exchange-rates.html')
        rate_data = self.parse(html_cont)
        self.add_rate(rate_data)


    def add_rate(self, rates):
        if rates is None or len(rates) == 0:
            return
        print(rates)

    def download(self, url):
        requests.adapters.DEFAULT_RETRIES = 3
        response = requests.get(url, timeout=3)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            return None
        return response.content.decode("utf-8")

    def parse(self, html_cont):
        print(html_cont)
        if html_cont is None:
            return
        data = []

        return data

def rate_job():
    obj_spider = ExchangeRateSpider()
    obj_spider.craw()


rate_job()