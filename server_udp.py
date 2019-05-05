# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:44:09 2019

@author: Alex1
"""

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server: Socket created')

host = 'localhost'
port = 6666

server_socket.bind((host,port))

while True:
    message, addr = server_socket.recvfrom(1024)
    
    if message:
        print('Message received from client: ', message.decode('utf-8'))
        server_socket.sendto(bytes("Hello client!", 'utf-8') + message, addr)
