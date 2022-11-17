import socket
import threading



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10002))
server.listen(2)    

def wait_for_client(server):
    global clientconnected
    print("Server is listening...")
    print ("Waiting for client...")
    while clientconnected == False:
        client, address = server.accept()
        print("Client connected: ", address)
        clientconnected = True
        client.send ("Hello Client".encode())

def receive_data(clientconnected):
    global client
    print(f"Client {clientconnected}")
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

def send_data(client):
    while clientconnected == True:
        data = input("Enter message to send to client: ")
        client.send(data.encode())
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

def main():
    global clientconnected
    global client
    clientconnected = False
    t1 = threading.Thread(target=wait_for_client, args=[server])
    t1.start()
    t1.join()
    t2 = threading.Thread(target=receive_data , args=[clientconnected])
    t2.start()
    t2.join()

    

if __name__ == '__main__':
    main()