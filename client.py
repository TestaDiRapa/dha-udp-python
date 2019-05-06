import socket

with open("conf.conf") as file:
    lines = file.readlines()
    conf = dict()
    for line in lines:
        param = line.split(':')
        conf[param[0]] = param[1][:-1]

IP = conf["ip"]
PORT = int(conf["port-c"])
PORT_SERVER = int(conf["port-s"])

choice = conf["type"]

if choice == "T":
    print("TCP mode")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((IP, PORT_SERVER))
    except:
        print("TCP connection error!")

else:
    print("UDP mode")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((IP, PORT))
    except:
        print("Port already in use!")

while True:
    msg = input("Insert a message: ")

    if choice == "T":
        s.sendall(msg.encode("utf-8"))
        response = s.recv(1024)

    else:
        s.sendto(bytes(msg, 'utf-8'), (IP, PORT_SERVER))
        response, address = s.recvfrom(1024)

    print("Response: {}".format(response.decode("utf-8")))

s.close()