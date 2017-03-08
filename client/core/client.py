#!/usr/bin/python
import socket
import time
import sys

'''
udp client for chat app.
notes(' try - except ')
'''
class Core:
    '''
    constructor
    notes(
        'nick support',
            )
    '''
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.remote = 0

    '''
    new server connection
    '''
    def create(self, host, port):
        self.remote = (host, port)

    '''
    receive data
    '''
    def get(self):
        data = self.sock.recv(1024)
        data = data.decode('utf-8')
        if data[0] == '/':
            return 0
        return data

    '''
    get data
    '''
    def post(self, data):
        data = data.encode('utf-8')
        self.sock.sendto(data, self.remote)

    '''
    other tweakZZ
    '''
    def pong(self):
        pass

    def disconnect(self):
        pass
