import socket

IP = "127.0.0.1"
PORT = int(input("Port: "))

choice = input("TCP or UDP? [T/U]: ")
while choice != "T" and choice != "U":
    choice = input("TCP or UDP? [T/U]: ")

if choice == "T":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(input("Port to connect?: "))
    s.connect((IP, port))

else:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP, PORT))

while True:
    msg = input("Insert a message: ")

    if choice == "T":
        s.sendall(msg.encode("utf-8"))
        response = s.recv(1024)

    else:
        port = int(input("Insert the port: "))
        s.sendto(bytes(msg, 'utf-8'), (IP, port))
        response, address = s.recvfrom(1024)

    print("Response: {}".format(response.decode("utf-8")))

s.close()