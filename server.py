# -*- coding:utf-8 -*-
import socket
# threading Process
import threading

host = "127.0.0.1"
port = 6000
client = []

# スレッドのサーバー処理
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
        # クライアント側が接続を切ったときの処理
        except ConnectionResetError:
            # ソケットを閉じる
            clientsock.close()
            # ソケットとアドレスを削除する
            client.remove((clientsock,address))

def server_start():
    # サーバ側の処理を起動する．
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind((host,port))
    serversock.listen(10)

    while True:
        clientcon, address = serversock.accept()
        # Client Append
        client.append((clientcon,address))
        # スレッドを作成する．クライアントのソケットとクライアント側のアドレスをわたす．
        thread_handler = threading.Thread(target=handler,args=(clientcon,address),daemon=True)
        # スレッドをスタートする．
        thread_handler.start()

if __name__ == "__main__":
    server_start()
