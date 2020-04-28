import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 60000))
serversocket.listen(0)
clientsocket, ad = serversocket.accept()
while True:
    data = clientsocket.recv(60000)
    clientsocket.send(data)
    print("받은 데이터 출력 : ", data.decode())
