# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/22 22:01


import requests
from models.ProxyServer import ProxyServer
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
import json


URL = "https://www.xicidaili.com/nn/"


def parse_page(text):
    soup = BeautifulSoup(text)
    trs = soup.find_all("tr")
    ip_list = []
    for tr in trs[1:]:
        tds = tr.find_all("td")
        ps = ProxyServer(tds[1].string, tds[2].string, ("未知" if tds[3].a == None else tds[3].a.string), tds[5].string,
                    tds[6].div['title'],tds[7].div['title'], tds[8].string,
                         time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                         tds[9].string, tds[4].string)
        # print(ps.toJson())
        ip_list.append(ps.toJson())
    return ip_list

def get_page(limit):
    ua = UserAgent(verify_ssl=False)
    ip_total = []
    for i in range(limit):
        print("Getting page " + str(i + 1))
        headers = {"User-Agent": ua.random}
        response = requests.get(url=URL + str(i + 1), headers=headers)
        ip_total.extend(parse_page(response.text))
        time.sleep(5)
    return ip_total

def crawl(limit):
    ip = get_page(limit)
    date_now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print(f"Got {len(ip)} piece of data.")
    try:
        with open('E:\\data\\ProxyServer\\' + date_now + '.json', 'wt', encoding="utf-8") as f:
            json.dump(ip, f, ensure_ascii=False, indent=4)
            print("Written to" + date_now + ".json")
        return (True, 'E:\\data\\ProxyServer\\' + date_now + '.json')
    except IOError:
        return (False, None)

if __name__ == "__main__":
    print("Getting some ProxyServer")
    crawl(1)


