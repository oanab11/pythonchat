from threading import Thread
from socket import socket


class Client:
    def __init__(self, ip, port, username):
        self.sock=socket()
        self.username=username
        self.serv_ip=ip
        self.port=port


    def connect(self):
        self.sock.connect((self.serv_ip,self.port))
        self.servername=self.sock.recv(1024)

        print("connected to %s on port %d \n say ceau to %s" % (self.serv_ip,self.port,self.servername))
        Thread(target=self.listen_for_messages).start()


    def listen_for_messages(self):
        while(True):
            print(self.sock.recv(1024))


    def send_messages(self):
        pass



