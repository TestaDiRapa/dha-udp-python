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


IP = "127.0.0.1"
PORT = int(input("Port: "))

choice = input("TCP or UDP? [T/U]: ")
while choice != "T" and choice != "U":
    choice = input("TCP or UDP? [T/U]: ")

if choice == "T":
    sock_type = socket.SOCK_STREAM
    handler = handle_tcp
else:
    sock_type = socket.SOCK_DGRAM
    handler = handle_udp

s = socket.socket(socket.AF_INET, sock_type)

s.bind((IP, PORT))
handler(s)
s.close()