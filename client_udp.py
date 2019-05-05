# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:55:43 2019

@author: Alex1
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ('Client Socket created')

host= 'localhost'
port=5547
message = input('insert the message:')

try:
    client_socket.sendto(message.encode(), (host,6666))
    
    message_r,server = client_socket.recvfrom(1024)
    message_r = message_r.decode()
    print('Response: '+ message_r)
    
finally:
    client_socket.close()

    
                              