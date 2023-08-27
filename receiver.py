import socket as sk
import os as os
import string as string

Host = '127.0.1.1'
Port = 9999
client_socket=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
client_socket.connect((Host, Port)) #address and port id of server

counter_number =0
client_socket.sendto(str(counter_number).encode('utf-8'),(Host, Port))
total_bytes=client_socket.recvfrom(1024)
print(total_bytes[0].decode())
bytes_received=0

file_name = 'data.txt'
while True:
    counter_number+=1
    if bytes_received!=total_bytes:
        client_socket.sendto(str(counter_number).encode('utf-8'),(Host, Port))
        data_segment = client_socket.recvfrom(1024)[0].decode()
        with open(file_name, 'a') as f:
            while data_segment!='\n':
                f.write(data_segment)
            f.write('\n')
        bytes_received=os.path.getsize(file_name)
    else :
        break

client_socket.close()
