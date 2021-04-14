# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import requests
import pymysql
import config


class ExchangeRateSpider(object):
    def craw(self):
        html_cont = self.download('https://www.services.cn-banking.hsbc.com.cn/PublicContent/common/rate/zh/exchange-rates.html')
        rate_data = self.parse(html_cont)
        self.add_rate(rate_data)


    def add_rate(self, rates):
        if rates is None or len(rates) == 0:
            return
        try:
            connection = pymysql.connect(**config.dbconfig)
            with connection.cursor() as cursor:
                sql = 'INSERT INTO cbg_role (yn,create_time'
                for key, value in role.items():
                    sql = sql + ',' + key
                sql += ' ) values (1,now()'
                for key, value in role.items():
                    if type(value) == int:
                        sql = sql + ',' + str(value)
                    else:
                        sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''
                sql += ')'
                self.log.logger.info(sql)
                cursor.execute(sql)
                connection.commit()
        except Exception as e:
            print(e)
            pass
        finally:
            connection.close()

    def download(self, url):
        requests.adapters.DEFAULT_RETRIES = 3
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text

    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []

        return data

def rate_job():
    obj_spider = ExchangeRateSpider()
    obj_spider.craw()
