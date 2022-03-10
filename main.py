#socket reference
#https://docs.python.org/3.3/library/socket.html

from Server import server
from Client import client
import _thread

_thread.start_new_thread(server('40:1C:83:B7:F6:D2',4))
_thread.start_new_thread(client('40:1C:83:B7:F6:D2',4))
#server setting
#server('40:1C:83:B7:F6:D2',4)
#client setting
#client('40:1C:83:B7:F6:D2',4)