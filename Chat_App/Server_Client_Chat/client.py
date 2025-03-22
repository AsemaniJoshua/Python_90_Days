import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 55555))

done = False
print("Client is ready to chat!")

while not done:
    # Send a message to the server
    send_msg = input("Client: ")
    client.send(send_msg.encode('utf-8'))
    # Receive a message from the server
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        done = True
        print("Server has disconnected.")
        client.close()
    else:
        print(f"Server: {msg}")
        