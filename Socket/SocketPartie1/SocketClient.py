import socket

# Create one client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10002))
print(f"Client connected to server")
client.send("Hello Server".encode())
data = client.recv(1024).decode()
print(data)

while True:
    message = input("Enter your message: ") # Possible to send message to the server
    client.send(message.encode())
    if message == "exit": # Close the server when client send "exit" message
        client.close()
        break
    elif message == "close": # Close the client connection but not down the server if client send "close"
        print ("Client disconnected")
        break

if __name__ == '__main__':
    pass

