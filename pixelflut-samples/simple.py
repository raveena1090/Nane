#!/usr/bin/env python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 1234))

def px(x, y, rgba='ffffffff'):
	sock.send('PX {} {} {}\n'.format(x, y, rgba))

px(23, 42)

