#!/usr/bin/python3
import socket
import threading
import time
import json
import sys

'''
Server
'''

class Engine():
    def __init__(self):

        self.sock = 0
        self.connections = []

    def createServer(self, ip, port, socktype = 'udp'):

        if socktype == 'udp':

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((socket.gethostname(), port))
            '''
            except:
                print("Failed to start the server.")
                print("Error: ")
                print(sys.exc_info()[0])
                return 0
            '''
            return 1

        else:
            print("tcp not available yet")
            return 0


    def get(self):
        data, addr = self.sock.recvfrom(1024)
        return data, addr

    '''
    sending bytes to single connections
    '''
    def post(self, data, client):
        '''
        data is the data to be sent ofc
        client is a list (ip, port)
        '''
        self.sock.sendto(data, client)

    '''
    broadcasting - sending bytes to all connections
    '''
    def broadcast(self, data):
        for conn in self.connections:
            self.sock.sendto(data, conn)

    '''
    keeping track of active connnections
    '''
    def onconnect(self, new):
        if new not in self.connections:
            self.connections.append(new)
    '''
    active connections watcher
    '''
    def ping(self):
        def getpong(client):
            data, address = self.sock.recvfrom(1024)
            '''
            Do some checking of response if needed here.
            '''
            if address == client:
                return 1
            else:
                return 0

        def check(client):
            data = "/ping"
            self.sock.sendto(data, client)
            active = getpong(client)
            if active == 1:
                return 1;
            else:
                return 0;
        i = 0

        for conn in self.connections:
            res = check(conn)
            if res == 0:
                '''
                delete connection if no response came back
                '''
                del self.connections[i]
            else:
                continue
