import socket
import threading
import os
import platform

# Create one client socket
def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 10008))
    return client

# Send the message to the server
def send_message(client):
    while True:
        message = input('Type your message: ')
        client.send(message.encode())
        if message == '{quit}':
            client.close()
            break


# Receive the message from the server
def receive_message(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message == '{quit}':
                client.close()
                break
            else:
                print(message)
        except:
            print('An error occured!')
            client.close()
            break

# Main function
def main():
    client = connect_to_server()
    threading.Thread(target=send_message, args=(client,)).start()
    threading.Thread(target=receive_message, args=(client,)).start()



if __name__ == '__main__':
    main()