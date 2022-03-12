#socket reference
#https://docs.python.org/3.3/library/socket.html

from Server import Server
from Client import Client
import threading
import time

server = Server('xx:xx:xx:xx:xx:xx',4)
client = Client('xx:xx:xx:xx:xx:xx',4)

t1 = threading.Thread(target=server.config_server)
t2 = threading.Thread(target=client.config_client)

t1.start()
t2.start()



#server.run()
#client.run()
#server setting
#server('40:1C:83:B7:F6:D2',4)
#client setting
#client('40:1C:83:B7:F6:D2',4)