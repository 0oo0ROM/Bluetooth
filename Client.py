'''
Python sockets client
mac: server's MAC
port: same as server's port number
'''

import socket

def client(mac, port):
    ServerMAC = mac
    port = port
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((ServerMAC, port))
    while 1:
        text = input()
        if text == "quit":
            break
        s.send(bytes(text, 'UTF-8'))
    s.close()