import socket
import os
import random
import string

Host = '127.0.8.1'
Port = 9999
print("the server is available")
server_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((Host, Port))

server_file = open("server.txt", "a")

for _ in range(100):
    server_file.write(str(random.randrange(0,100)))


with open('input.txt', 'r') as f:
    lines = f.readlines()
with open('server.txt', 'w') as f:
    for line in lines:
        random_char = random.choice(string.ascii_letters)
        f.write(random_char + line)

while True:
    data, client_address = server_socket.recvfrom(1024)
    if not data:
            break
    else:
        print(f"{data.decode('utf-8')} is received")
        next_packet = int(data.decode('utf-8'))
        server_socket.sendto(data, client_address)

server_socket.close()

