import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))

server.listen()
client, address = server.accept()
print(f"Connection from {address} has been established!")

done = False
print("Server is ready to chat!")

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        done = True
        print("Client has disconnected.")
        client.close()
        server.close()        
    else:
        print(f"Client: {msg}")
        send_msg = input("Server: ")
        client.send(send_msg.encode('utf-8'))
