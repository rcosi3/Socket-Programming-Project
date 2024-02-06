import socket

#Talking over public internet (not LAN) visit myip.is
#firewall needs to be open

#gets private ip
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 9999

#specify protocol
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect finction uses connect instead of bind
socket.connect((HOST, PORT)) #also in tuple

#encode sended message
socket.send("Hello World!".encode('utf-8'))
#show recieved message
print(socket.recv(1024).decode('utf-8'))
