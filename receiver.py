import socket as sk
import os as os

Host = '127.0.11.1' # The IP address should match the server's IP address
Port = 9999
client_socket=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
client_socket.connect((Host, Port)) #address and port id of server

counter_number =0
client_socket.sendto(str(counter_number).encode('utf-8'),(Host, Port))
total_bytes, _=client_socket.recvfrom(1024)
total_bytes = int(total_bytes)
print(total_bytes)
bytes_received=0

file_name = 'DataReceived.txt'
while True:
    counter_number+=1
    if bytes_received != total_bytes:
        client_socket.sendto(str(counter_number).encode('utf-8'),(Host, Port))
        data_segment, _ = client_socket.recvfrom(1024)
        print(f"{data_segment} is received")
        with open(file_name, 'ab') as f: # The file should be opened in append binary mode to write the received bytes
            f.write(data_segment)
        bytes_received=os.path.getsize(file_name)
        print(bytes_received)
    else :
        break
client_socket.close()
