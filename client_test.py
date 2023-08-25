import socket

Host = '127.0.8.1'
Port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

number = 0
number_bytes = str(number).encode()

client_socket.sendto(number_bytes, (Host, Port))

while True:
    if int(client_socket.recvfrom(1024)[0].decode()) == number:
        number = number + 1
        number_bytes = str(number).encode()
        client_socket.sendto(number_bytes, (Host, Port))
    else:
        break

client_socket.close()
