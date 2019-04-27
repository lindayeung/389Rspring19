#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = open("hashes.txt").read().splitlines() # open and read hashes.txt
    passwords = open("passwords.txt").read().splitlines() # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)

    # crack 3 times
    for i in range(1, 4):
        # parse data
        data = string.split(data, '\n')
        data = data[2]

        for c in characters:
            for p in passwords:
                if hashlib.sha256(c + p).hexdigest() == data:
                    s.send(c + p + '\n')
        data = s.recv(1024)

    print(data)

if __name__ == "__main__":
    server_crack()
