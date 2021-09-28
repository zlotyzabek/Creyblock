import socket
import sys
import pickle

class ServerConecting:
    def __init__(self, conn, addr):

        self.gamePath = sys.path[0]

        with open(f'{self.gamePath}/assest/saves/save/worldSave.data', 'rb') as filehandle:
            self.blockFileRead = pickle.load(filehandle)

        with conn:
            print('Got connection from: ', addr)
            while True:
                data = conn.recv(1024).decode("utf-8")

                if data[0] == "r":
                    conn.sendall(bytes(str(self.blockFileRead[int(data[1:])]), 'utf-8'))

s = socket.socket()
print ("Server created")

port = 12345
host = "127.0.0.1"

s.bind((host, port))
print (f"Server Started on port: {port}")

s.listen()
print ("Waiting for client")

conn, addr = s.accept()
ServerConecting(conn, addr)



