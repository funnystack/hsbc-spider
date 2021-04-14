# hsbc-spider
汇丰银行汇率爬虫




crontab –e 
0 */1 * * * sh /usr/local/txspider/start_role.sh >> /var/log/spider.log 2>&1
