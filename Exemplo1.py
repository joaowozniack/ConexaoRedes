#!/usr/bin/env python 3

import socket
import sys

HOST = '127.0.0.1'  # localhost = esta máquina
PORT = int(input('Digite a porta do servidor: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except:
    print("# erro de bind")
    sys.exit()

s.listen(5)

print('aguardando conexões em ', PORT)
conn, addr = s.accept()

print('recebi uma conexão de ', addr)

while True:
    conn, addr = s.accept()
    print('recebi uma conexão de ', addr )

    while True:
        data = conn.recv(1024)
        print('recebi', len(data), ' bytes')

        if not data:
            break
        print(data)

print('o cliente encerrou')
conn.close()