# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/22 22:01


import requests
from models.ProxyServer import ProxyServer
from fake_useragent import UserAgent
import time


URL = "https://www.xicidaili.com/nn/"


def parse_page(text):
    # TODO
    return

def get_page(limit):
    ua = UserAgent(use_cache_server=False)
    for i in range(limit):
        print("Getting page " + str(i + 1))
        headers = {"User-Agent": ua.random}
        response = requests.get(url=URL + str(i + 1), headers=headers)
        parse_page(response.text)
        time.sleep(5)

if __name__ == "__main__":
    print("Getting some ProxyServer")
    get_page(20)

