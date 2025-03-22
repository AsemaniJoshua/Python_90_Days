import socket
import threading

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server.bind(('127.0.0.1', 55555))

# Listen for incoming connections
server.listen()

# List of clients and usernames
clients = []
usernames = []

# Broadcast function
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle client connections
def handle_client(client):
    while True:
        try:
            # Broadcast messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove and close clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            broadcast(f"{username} left the chat".encode('utf-8'))
            break

# Main server loop
def start_server():
    print("Server is running and waiting for connections...")
    while True:
        client, address = server.accept()
        print(f"Connection from {address} has been established!")
        client.send('Enter your USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username of the client is {username}.")
        
        client.send('Connected to the server! You can start chatting!!'.encode('utf-8'))
        broadcast(f"{username} joined the chat!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Start the server using threading
server_thread = threading.Thread(target=start_server)
server_thread.start()
    
