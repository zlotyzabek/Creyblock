# first of all import the socket library
import socket

s = socket.socket()
print ("Server created")

port = 12345

s.bind(('', port))
print (f"Server Started on port: {port}")

s.listen(5)
print ("Waiting for client")

c, addr = s.accept()
print ('Got connection from: ', addr)

c.send(b'Connecting')
print(c.listen())


