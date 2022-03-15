# hsbc-spider
汇丰银行汇率爬虫


pip install -r requirements.txt

crontab –e 
* * */6 * * sh /usr/local/hsbc-spider/start.sh >> /usr/local/hsbc-spider/spider.log 2>&1
