import socket
import ast

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        s.sendall(bytes(input("->"), 'utf-8'))
        print(ast.literal_eval(s.recv(10240).decode("utf-8")))
