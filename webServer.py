###importing socket module
from socket import *  

#Passing an empty string means that the server can listen to incoming connections from other computers as well.
HOST = "192.168.1.208" 
PORT = 5050 # Assign a port number



###creating socket
try:
    serverSocket = socket(AF_INET, SOCK_STREAM) 
    #(family parameter-> telling the socket what kind of address we gonna be accepting)AF_INET is used for IPv4 protocols
    #(type parameter) SOCK_STREAM is used for TCP)
except socket.error as err:
    print("Failed to create server socket")
   



###Prepare a sever socket
#Fill in start

serverSocket.bind((HOST,PORT))  #bind the server ip address & server port number
# Listen to at most 5 connections at a time
serverSocket.listen(5) #queue the rest of the requests while handling another request


#Fill in end

# Server should be up and running and listening to the incoming connections
while True:

###Establish the connection
    print ("Ready to serve...")

    # Set up a new connection from the client -> client has done socket connect & server socket accepted the connection
    (connectionSocket, addr) = serverSocket.accept()  
    
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed

    try:
        #Receives the request message from the client of (5000 characters)
        #you got the whole thing(get request, optional parameters), so you have to split it
        #get request on new line then header header header header header header then a blank line
        message = connectionSocket.recv(5000)

        # Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
        fileName = message.split()[1]

        # Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
        f = open(fileName[1:]) 

        # Read the file "f" and store the entire content of the requested file in a temporary buffer
        outputdata = f.read()

        #construct a response
        ###Send one HTTP header line into socket

        #Fill in start
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
        #Fill in end

        ###Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        
    except IOError:
        print("File not found")
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
    except KeyboardInterrupt:
        print("Shut down")
    except Exception as ex:
        print("Error: ")

print("Access http://localhost:5050")   