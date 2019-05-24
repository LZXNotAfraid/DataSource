# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/22 22:01


import requests
from models.ProxyServer import ProxyServer
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup


URL = "https://www.xicidaili.com/nn/"


def parse_page(text):
    soup = BeautifulSoup(text)
    trs = soup.find_all("tr")
    for tr in trs[1:]:
        tds = tr.find_all("td")
        ps = ProxyServer(tds[1].string, tds[2].string, ("未知" if tds[3].a == None else tds[3].a.string), tds[5].string,
                    tds[6].div['title'],tds[7].div['title'], tds[8].string,
                    time.time(), tds[9].string, tds[4].string)
        print(str(ps))
    return

def get_page(limit):
    ua = UserAgent(verify_ssl=False)
    for i in range(limit):
        print("Getting page " + str(i + 1))
        headers = {"User-Agent": ua.random}
        response = requests.get(url=URL + str(i + 1), headers=headers)
        parse_page(response.text)
        time.sleep(5)

if __name__ == "__main__":
    print("Getting some ProxyServer")
    get_page(1)

