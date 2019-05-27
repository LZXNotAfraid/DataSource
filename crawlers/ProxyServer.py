# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/27 23:31


from sqlalchemy import Column, DateTime, Float, String, create_engine
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
import requests
import datetime
from informer.EmailInformer import EmailInformer


URL = "https://www.xicidaili.com/nn/"
Base = declarative_base()
metadata = Base.metadata
engine = create_engine("mysql+pymysql://root:@/ProxyServer")
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Ip(Base):
    __tablename__ = 'ips'

    id = Column(INTEGER(10), primary_key=True)
    ip = Column(String(20), nullable=False)
    port = Column(String(10), nullable=False)
    location = Column(String(20), nullable=False)
    http_type = Column(String(20), nullable=False)
    speed = Column(Float(asdecimal=True), nullable=False)
    connect_time = Column(Float(asdecimal=True), nullable=False)
    survive_time = Column(String(20), nullable=False)
    collect_time = Column(DateTime, nullable=False)
    test_time = Column(String(30), nullable=False)
    hidden = Column(String(20), nullable=False)

    def __init__(self, ip, port, location, http_type, speed, connect_time, survive_time, collect_time, test_time, hidden):
        self.ip = ip
        self.port = port
        self.location = location
        self.http_type = http_type
        self.speed = speed
        self.connect_time = connect_time
        self.survive_time = survive_time
        self.collect_time = collect_time
        self.test_time = test_time
        self.hidden = hidden

    def __repr__(self):
        return (f"host:{self.ip}:{self.port} {self.hidden} @{self.location} "
                f"with speed@{self.speed} test_time{self.test_time} "
                f"connect_time@{self.connect_time} survive_time@{self.survive_time}"
                f" collected@{self.collect_time}")

    def toJson(self):
        re = {
            "address": self.ip,
            "port": self.port,
            "location": self.location,
            "http_type": self.http_type,
            "speed": self.speed,
            "connect_time": self.connect_time,
            "survive_time": self.survive_time,
            "collect_time": self.collect_time,
            "test_time": self.test_time,
            "hidden": self.hidden
        }
        return re


def parse_page(text):
    soup = BeautifulSoup(text)
    trs = soup.find_all("tr")
    ip_list = []
    for tr in trs[1:]:
        tds = tr.find_all("td")
        ps = Ip(tds[1].string,
                tds[2].string,
                ("未知" if tds[3].a == None else tds[3].a.string),
                tds[5].string,
                float(tds[6].div['title'][:-1]),
                float(tds[7].div['title'][:-1]),
                tds[8].string,
                datetime.datetime.now(),
                datetime.datetime.strptime("20" + tds[9].string, "%Y-%m-%d %H:%M"),
                tds[4].string)
        ip_list.append(ps)
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
    '''try:
        with open('E:\\data\\ProxyServer\\' + date_now + '.json', 'wt', encoding="utf-8") as f:
            json.dump(ip, f, ensure_ascii=False, indent=4)
            print("Written to" + date_now + ".json")
        return (True, 'E:\\data\\ProxyServer\\' + date_now + '.json')
    except IOError:
        return (False, None)'''
    session.add_all(ip)
    session.commit()
    session.close()
    print(f"Insert {len(ip)} piece of data")
    return len(ip)

if __name__ == "__main__":
    print("ProxyServer On Going")
    re = crawl(2)
    EmailInformer(f"共爬取{re}条数据",
                  "632814252@qq.com",
                  "爬虫反馈").send()
