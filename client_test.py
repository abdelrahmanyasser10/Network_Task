import socket

Host = '127.0.1.1'
Port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
number = 0

client_socket.sendto(number, (Host, Port))

while True:
    if client_socket.recvfrom(1024)[0].decode() == str(number):
        client_socket.sendto(str(number).encode(), (Host, Port))
    else:
        break

client_socket.close()