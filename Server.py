import socket
import threading


class Server:
    def __init__(self, mac, port):
        self.HostMAC = mac
        self.port = port
        self.backlog = 1
        self.size = 1024

    def config_server(self):
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((self.HostMAC, self.port))
        s.listen(self.backlog)
        try:
            client, address = s.accept()
            while 1:
                data = client.recv(self.size)
                if data:
                    print(data)
                    client.send(data)
        except:
            print("Closing socket")
            client.close()
            s.close()

    def run(self):
        t1 = threading.Thread(target=self.config_server)
        t1.start()