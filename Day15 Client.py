# Day 15: Introduction to Networking
# - Topics:
# - Introduction to sockets and networking.
# - Understanding IP addresses, ports, and how to connect to a server.
# - Project:
# - Write a simple TCP client-server application using Python’s socket module.

# Importing socket library
import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name (hostname) and define the port
    host = socket.gethostname()
    port = 9999

    # Connecting to server
    client_socket.connect((host, port))

    # Receiving message from the server and displaying it
    message = client_socket.recv(1024)
    print(message.decode("utf-8"))

    # Closing the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()

