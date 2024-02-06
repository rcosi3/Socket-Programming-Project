import socket as soc

#private ip
#can "localhost" instead if hosting on this computer only(no other computers)
HOST = '192.168.1.41'

#no well known ports
PORT = 9999

#specify socket (internet, TCP) to wait for connections
server = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
server.bind((HOST, PORT)) #passed as tuple
server.listen(5) # 5 connections before rejection

while True:
    communcation_socket, address = server.accept() #gives socket to talk to client, address of client
    print(f"Connected to {address}")

    #messages sent via socket are in byte streams (byte size 1024 here)
    #need to be encoded and decoded (ascii, utf-8)
    message = communcation_socket.recv(1024).decode('utf-8')
    print(f"Client Message: {message}")
    communcation_socket.send(f"Got your message! Thanks!".encode('utf-8')) #encode when sending
    communcation_socket.close()
    print(f"Connection with {address} terminated!")
