import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

while True:
    global data
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    while True:
        data = client_socket.recv(1024)
        print(data.decode())
        if data.decode() == 'exit':
            break
        else:
            client_socket.send(data)
    if data.decode() == 'exit':
        break

client_socket.close()
