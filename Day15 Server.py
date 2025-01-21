# Day 15: Introduction to Networking
# - Topics:
# - Introduction to sockets and networking.
# - Understanding IP addresses, ports, and how to connect to a server.
# - Project:
# - Write a simple TCP client-server application using Python’s socket module.

# importing socket library
import socket

# def start_server():
#
#     # Creating server socket
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Creating hostname and port number
#     host = socket.gethostname()
#     port = 9999
#
#     # Bind the socket to the host and port
#     server_socket.bind((host, port))
#
#     # Listen for incoming connections (max 5)
#     server_socket.listen(5)
#
#     print(f"Server started on {host}:{port}. Waiting for connections...")
#
#     # Accept a connection
#     client_socket, addr = server_socket.accept()
#     print(f"Connection from {addr} has been established")
#
#     # send a welcome message to the client
#     message = "Thanks for connecting!"
#     client_socket.send(message.encode("utf-8"))
#
#     # Closing socket
#     client_socket.close()
#
# if __name__ == "__main_":
#     start_server()


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name (hostname) and define the port
    host = socket.gethostname()
    port = 9999

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 5)
    server_socket.listen(5)

    print(f"Server started on {host}:{port}. Waiting for connections...")

    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    # Send a welcome message to the client
    message = "Thank you for connecting!"
    client_socket.send(message.encode('utf-8'))

    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    start_server()


