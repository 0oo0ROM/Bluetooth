'''
Python sockets client
mac: server's MAC
port: same as server's port number
'''

import socket
import threading


class Client:
    def __init__(self, mac, port):
        self.ServerMAC = mac
        self.port = port

    def config_client(self):
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect((self.ServerMAC, self.port))
        while 1:
            text = input()
            if text == "quit":
                break
            s.send(bytes(text, 'UTF-8'))
        s.close()

    def run(self):
        t1 = threading.Thread(target=self.config_client)
        t1.start()