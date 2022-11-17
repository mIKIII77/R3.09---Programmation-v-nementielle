import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10002))
server.listen(5)
print("Server is listening...")
clientconnected = False
print ("Waiting for client...")

# Wait for a client to connect
while clientconnected == False:
    client, address = server.accept()
    print("Client connected: ", address)
    clientconnected = True
    client.send ("Hello Client".encode())

# Receive data from the client when client connected
while clientconnected == True:
    data = client.recv(1024).decode()
    print(f"Client {address} send: {data}")
    if data == "exit": # Close the connection when client send "exit" message
        server.close()
        print (f"Server closed by {address}")
        break
    elif data == "close":  # Close the client connection but not the server if client send "close"
        print("Client disconnected")
        client.close()
        clientconnected = False 
        print ("Waiting for client...")
        while clientconnected == False: # Wait for a new client to connect
            client, address = server.accept()
            print("Client connected: ", address)
            clientconnected = True
            client.send ("Hello Client".encode())

if __name__ == '__main__':
    pass

