import socket

def server(mac,port):
    HostMAC = mac
    port = port
    backlog = 1
    size = 1024
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.bind((HostMAC, port))
    s.listen(backlog)
    try:
        client, address = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                client.send(data)
    except:
        print("Closing socket")
        client.close()
        s.close()