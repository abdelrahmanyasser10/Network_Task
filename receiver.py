import socket

Host = '127.0.8.1'
Port = 9999
print("the server is available")
server_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((Host, Port))

last_packet = 0

while True:
    data, client_address = server_socket.recvfrom(1024)
    if not data:
            break
    else:
        print(f"{data.decode('utf-8')} is received")
        next_packet = int(data.decode('utf-8'))
        server_socket.sendto(data, client_address)
    if next_packet == last_packet + 1:
        last_packet = next_packet

server_socket.close()

