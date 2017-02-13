#!/usr/bin/python3
from core.app.engine import Engine
'''
UDP chat server
'''
class Chat():

    def __init__(self):
        self.Server = Engine()
        self.Server.createServer('127.0.0.1', 4444, 'udp')
        print(self.Server)
        self.loop()

    def loop(self):
        while 1:
            data, addr  = self.Server.get()
            self.Server.onconnect(addr)
            self.Server.broadcast(data)
            print(data)

cl = Chat()
