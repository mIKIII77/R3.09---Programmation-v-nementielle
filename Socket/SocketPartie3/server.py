import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10008))
server.listen(5)    

 # Automatically accept the connection of many clients
def accept_clients():
    global client
    while True:
        client, addr = server.accept()
        print('Connected to ', addr)
        client.send('Welcome to the server!'.encode())
        client.send('Type your name and press enter!'.encode())
        threading.Thread(target=handle_client, args=(client,)).start()

 # Handle the client
def handle_client(client):
    global clients
    global name
    name = client.recv(1024).decode()
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(welcome.encode())
    msg = '%s has joined the chat!' % name
    broadcast(msg.encode())
    clients[client] = name
    while True:
        msg = client.recv(1024)
        if msg != '{quit}':
            broadcast(msg, name + ': ')
        else:
            client.send('{quit}'.encode())
            client.close()
            del clients[client]
            broadcast('%s has left the chat.' % name)
            break

 # Broadcast the message to all clients
def broadcast(msg, prefix=''):
    global clients
    for sock in clients:
        if sock != client:
            sock.send(prefix.encode() + msg)



def main():
    print('Server is running...')
    global clients
    global msg
    clients = {}
    msg = ''
    t1 = threading.Thread(target=accept_clients, args=[])
    t1.start()
    t3 = threading.Thread(target=broadcast, args=[msg])
    t3.start()







if __name__ == '__main__':
    main()