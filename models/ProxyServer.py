# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/21 23:31

from IPy import IP
import time

class ProxyServer:

    address = IP('0.0.0.0')
    port = 0
    location = ''
    http_type = ''
    speed = 0
    connect_time = 0
    survive_time = 0
    collect_time = None
    test_time = None
    hidden = False

    def __init__(self, address, port, location, http_type, speed, connect_time, survive_time, collect_time, test_time, hidden):
        self.address = address
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
        return (f"host:{self.address}:{self.port} {self.hidden} @{self.location} "
                f"with speed@{self.speed} test_time{self.test_time} "
                f"connect_time@{self.connect_time} survive_time@{self.survive_time}"
                f" collected@{self.collect_time}")


    def toJson(self):
        return {
            "address": self.address,
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
