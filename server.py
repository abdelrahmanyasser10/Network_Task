import socket

Host = socket.gethostbyname(socket.gethostname())
Port = 9999
print("the server is available")
server_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((Host, Port))
global number
number = 0

while True:
    number, client_address = server_socket.recvfrom(1024)
    if number == "exit":
            break
    else:
        print(f"{number.decode()} is received")
        server_socket.sendto(number.encode(), client_address)
server_socket.close()

