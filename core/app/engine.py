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
        if data.decode('utf-8')[0] == '/':
            self.switch(data.decode('utf-8'), addr)
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
        print("Client checking... ")
        self.stop = 1
        self.current = ""
        while 1:
            for remote in self.connections:
                self.current = remote
                print(self.current[0])
                self.post("/ping".encode('utf-8'), remote)
                end_t = int(time.time() + 5)

                while int(time.time()) <= end_t:
                    print( 'a' )

                print("end time: " + str(int(end_t)))
                if self.stop == 1:
                    '''
                    remove client
                    '''
                    self.connections.remove(remote)
                    print("client: " + remote[0] + " deleted")

                self.stop = 1
            time.sleep(5)

    def pong(self, remote):
        if remote == self.current:
            self.stop = 0


    def switch(self, do, arg):
        options = {
            "pong" : self.pong,
        }

        if command[1:] in options:
            options[command[1:]](arg)
        else:
            pass
