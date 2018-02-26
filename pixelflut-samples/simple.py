#!/usr/bin/env python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 1234))

def px(x, y, rgba="ffffffff"):
    data = "PX {} {} {}\n".format(x, y, rgba).encode('ascii')
    sock.send(data)

for i in range(42,100) :
	px(23, i)
	i = i+1

for i in range(23,100) :
	px(i, 42)
	i = i+1

for i in range(42,100) :
	px(100,i)
	i = i+1
for i in range(23,100) :
	px(i,100)
	i = i+1