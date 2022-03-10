#socket reference
#https://docs.python.org/3.3/library/socket.html

from Server import Server
from Client import Client
import threading
import time

server = Server('40:1C:83:B7:F6:D2',4)
client = Client('C0:3C:59:A8:A6:B9',4)
server.run()
client.run()
#server setting
#server('40:1C:83:B7:F6:D2',4)
#client setting
#client('40:1C:83:B7:F6:D2',4)