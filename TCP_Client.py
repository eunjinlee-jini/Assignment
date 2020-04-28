import socket
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(('127.0.0.1', 60000))
while True:
    data1=input()
    clientsock.send(data1.encode())
    data2=clientsock.recv(60000)
    print("돌려받은 데이터 출력 : ", data2.decode())
