# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/21 23:31

from IPy import IP
import time

class ProxyServer:

    address = IP('0.0.0.0')
    port = 0
    connectivity = -1
    location = ''
    http_type = ''
    speed = 0
    connect_time = 0
    survive_time = 0
    test_time = time.time(0)

    def __init__(self, address, port, connectivity, location, http_type, speed, connect_time, survive_time, test_time):
        self.address = address
        self.port = port
        self.connectivity = connectivity
        self.location = location
        self.http_type = http_type
        self.speed = speed
        self.connect_time = connect_time
        self.survive_time = survive_time
        self.test_time = test_time


