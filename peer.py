
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = int(input("Insert the port: "))
multi_group = ('224.3.29.71', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    try:
        print("Received: {}".format(sock.recvfrom(1024)))
    except socket.timeout:
        print("No messages")
    mess = input("Message: ")
    port = int(input("Port: "))
    sock.sendto(bytes(mess, 'utf-8'), (UDP_IP, port))
