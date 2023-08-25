import socket

Host = '127.0.8.1'
Port = 9999
print("the server is available")
server_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((Host, Port))

while True:
    data, client_address = server_socket.recvfrom(1024)
    if data == "exit":
            break
    else:
        print(f"{data.decode()} is received")
        server_socket.sendto(data, client_address)
server_socket.close()

