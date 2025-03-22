import socket
import threading

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 55555))

# Get the username
username = input("Enter your username: ")


# Receive and print messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Enter your USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Send messages to the server
def send_messages():
     while True:
        message = input('')
        client.send(f"{username}: {message}".encode('utf-8'))

# Create threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

# Start the threads
receive_thread.start()
send_thread.start()