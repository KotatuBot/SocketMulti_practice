# SocketMulti_practice
## ServerSocketでの複数クライアント

1. 複数クライアントをsocketで実装するにはスレッド間通信を行う必要がある．=> threadingライブラリを利用する．
2. handler関数としてクライアント側の処理を置く(readやwrite)
3. handler関数には，acceptしたクライアント側のソケットとアドレスを受け取りConnectionResetを受け取った際にクライアントを削除する．
4. threading関数には，handler関数を設定する．
