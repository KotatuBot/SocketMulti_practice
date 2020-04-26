# -*- coding:utf-8 -*-
import socket
# threading Process
import threading

host = "127.0.0.1"
port = 6000
client = []

def handler(clientsock,address):
    while True:
        try:
            # Read => Server
            rcvmsg = clientsock.recv(4096)
            rcvmsg=rcvmsg.decode("utf-8")
            print ('Received -> %s' % (rcvmsg))
            if rcvmsg == '':
              break
            print ('Recepi message...')
            s_msg = "Get answer"
            s_msg=s_msg.encode("utf-8")
            # Write => Client
            clientsock.send(s_msg)
            print ("send message")
        except ConnectionResetError:
            clientsock.close()
            # Remove Client Socket
            client.remove((clientsock,address))

def server_start():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind((host,port))
    serversock.listen(10)

    while True:
        clientcon, address = serversock.accept()
        # Client Append
        client.append((clientcon,address))
        # Client Socket Tread Client
        thread_handler = threading.Thread(target=handler,args=(clientcon,address),daemon=True)

        thread_handler.start()

if __name__ == "__main__":
    server_start()
