import socket
import os
import random
import string


def main():
    server_socket = setting_udp_server()
    generate_file()
    send_bytes(server_socket)
    print("Thanks for using our Server!!")

def setting_udp_server():
    host = '127.0.11.1'
    port = 9999
    print("the server is available")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    return server_socket

def generate_file():
    file_name = 'server.txt'
    with open(file_name, 'a') as f:
        for _ in range(0, 100):
            f.write('\n')

    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name, 'w') as f:
        f.write(lines[0])  # new line
        for line in lines[1:]:
            random_number = random.randrange(0, 100)
            f.write(str(random_number) + line)

    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name, 'w') as f:
        f.write(lines[0])
        for line in lines[1:]:
            random_char = random.choice(string.ascii_letters)
            f.write(random_char + line)

def getting_file_size():
    file_name = "server.txt"
    file_size = 0
    try:
        file_size = os.path.getsize(file_name)
        print(f"File Size in Bytes is {file_size}")
    except FileNotFoundError:
        print("File not found.")
    except OSError:
        print("OS error occurred.")
    return file_size

def send_bytes(server_socket):
    count = 0
    file_name = "server.txt"
    file_size = getting_file_size()
    while True:
        requested_packet, receiver_address = server_socket.recvfrom(1024)
        if requested_packet == b'0':
            server_socket.sendto(str(file_size).encode('utf-8'), receiver_address)
            print(f"{file_size} is sent")

        else:
            with open(file_name, 'rb') as f:
                byte = f.read(1)
                while byte != b"":
                    print(byte + b' is sent')
                    server_socket.sendto(byte, receiver_address)
                    count += 1
                    byte = f.read(1)
            print(f"{count} of bytes sent")
            break
    server_socket.close()

if __name__ == "__main__":
    main()
