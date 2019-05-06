from threading import Thread
import socket


def handle_tcp(s):
    s.listen(1)
    while True:
        client_socket, address = s.accept()
        print("Connection incoming from {}".format(address))
        Thread(target=handle_tcp_client, args=(client_socket, )).start()


def handle_tcp_client(conn):
    while True:
        data = conn.recv(1024)
        data = "ECHO: " + data.decode("utf-8")
        conn.sendall(data.encode("utf-8"))
    conn.close()


def handle_udp(s):
    while True:
        msg, address = s.recvfrom(1024)
        msg = "ECHO: " + msg.decode("utf-8")
        s.sendto(bytes(msg, "utf-8"), address)


with open("conf.conf") as file:
    lines = file.readlines()
    conf = dict()
    for line in lines:
        param = line.split(':')
        conf[param[0]] = param[1][:-1]

IP = conf["ip"]
PORT_SERVER = int(conf["port-s"])
choice = conf["type"]

if choice == "T":
    print("TCP mode")
    sock_type = socket.SOCK_STREAM
    handler = handle_tcp
else:
    print("UDP mode")
    sock_type = socket.SOCK_DGRAM
    handler = handle_udp

s = socket.socket(socket.AF_INET, sock_type)

try:
    s.bind((IP, PORT_SERVER))
except:
    print("Bind error!")

handler(s)
s.close()