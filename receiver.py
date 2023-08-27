import socket as sk

socket_c=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
socket_c.connect(('127.0.1.1', 9999)) #address and port id of server

starting_number =0
while 1:
    starting_number+=1
    socket_c.sendto(str(starting_number).encode('utf-8'),('127.0.1.1', 9999))
    server_msg=socket_c.recvfrom(1024)
    print(server_msg[0])

socket_c.close()
