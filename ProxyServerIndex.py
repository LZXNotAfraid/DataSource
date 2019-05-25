# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/25 13:32

from crawlers import ProxyServerCrawler
import time
from informer.EmailInformer import EmailInformer

if __name__ == "__main__":
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(f"Crawler ProxyServer start @ {timestamp}")
    message = ""
    re = ProxyServerCrawler.crawl(1)
    if re[0]:
        message = f"文件保存成功，{re[1]}"
    else:
        message = "文件保存失败"
    e = EmailInformer(message, "632814252@qq.com", "爬虫反馈", [re[1]])
    e.send()
