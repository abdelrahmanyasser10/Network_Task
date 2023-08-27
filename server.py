import socket
import os
import random
import string

Host = '127.0.1.1'
Port = 9999
print("the server is available")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((Host, Port))

file_name ='server.txt'
with open(file_name, 'a') as f:
    for _ in range(0, 100):
        f.write('\n')
#created 100 new lines in file

with open(file_name, 'r') as f:
    lines = f.readlines()
#read lines and return them as strings in list

with open(file_name, 'w') as f:
    f.write(lines[0]) #new line 
    for line in lines[1:]:
        random_number = random.randrange(0,100)
        f.write(str(random_number) + line)
#filling 99 lines with 99 random numbers in new lines

with open(file_name, 'r') as f:
    lines = f.readlines()
#read lines after filling and store in lines list 

with open(file_name, 'w') as f:
    f.write(lines[0])
    for line in lines[1:]:
        random_char = random.choice(string.ascii_letters)
        f.write(random_char + line)
#adding random ascii characters to each line 

global file_size
try:
    file_size = os.path.getsize(file_name)
    print(f"File Size in Bytes is {file_size}")
except FileNotFoundError:
    print("File not found.")
except OSError:
    print("OS error occurred.")

count = 0

while True:
    requested_packet, receiver_address = server_socket.recvfrom(1024)
    if requested_packet == '0':
        server_socket.sendto(str(file_size).encode('utf-8'), receiver_address)

    else:
        with open(file_name, 'rb') as f:
            byte = f.read(1)
            while byte != b"":
                print(byte + b' is sent')
                packet = server_socket.sendto(byte, receiver_address)
                count += 1
                byte = f.read(1)
        break
server_socket.close()

