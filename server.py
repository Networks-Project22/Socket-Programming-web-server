##import socket module
from socket import *
import sys      ##In order to terminate the program

##Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)     
#(family parameter -> telling the socket what kind of address we gonna be accepting)
#AF_INET is used for IPv4 protocols
#(type parameter) SOCK_STREAM is used for TCP)
#for UDP -> socket.SOCK_DGRAM

host = "localhost"
port = 8888
serverSocket.bind((host, port))
serverSocket.listen(5)
###Prepare a sever socket

##Establish the connection 
print('Ready to serve...') 
connectionSocket, addr = serverSocket.accept()
print("accept from ", addr)
try:
    message = connectionSocket.recv(1024).decode()
    print(message)
    filename = message.split()[1][1:]
    with open(filename) as f:
        outputdata = f.read()
    ##Send one HTTP header line into socket
    connectionSocket.sendall("HTTP/1.1 200 ok\r\n".encode())
    connectionSocket.send("\r\n".encode())
    
    ##Send the content of the requested file to the client 
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode()) 
    connectionSocket.send("\r\n".encode())
except IOError:
    ##Send response message for file not found
    print("file not find")
    connectionSocket.sendall("HTTP/1.1 404 not found\r\n".encode())
    connectionSocket.send("\r\n".encode())
    #send: sends as much data as the recv can hold
    #sendall: continues to send untill the buffer is empty 
    #(buffer:region of a memory used to temporarily store data while it is being moved from one place to another)
connectionSocket.close()

serverSocket.close()
sys.exit()##Terminate the program after sending the corresponding data