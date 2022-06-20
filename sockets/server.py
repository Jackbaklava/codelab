import socket
import threading # A way of creating multiple threads in a single python program

# Max size of a message in bytes
HEADER = 64
MSG_FORMAT = "utf-8"

# Automatically gets our local IPv4 adress
# socket.gethostname() -> Returns computer's name
HOST = socket.gethostbyname(socket.gethostname())

# Local IPv4 address from ipconfig
# HOST = "192.168.10.105" (Hard-coded is not good)
# Non-privileged ports are > 1023
PORT = 5050

# Creates a socket
# 1st arg: family of IP adress (AF_INET is IPv4)
# 2nd arg: type of socket (SOCK_STREAM uses TCP, allowd two-way comm. and data arrives synchronized)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binds server to address, anything that interacts with this address will interact with the socket 
server.bind((HOST, PORT))

# Handles communication between class and server, will run concurrently for each client
def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} connected")
    connected = True

    while connected:
        # Waits to recieve something from client and so also blocks execution, returns a byte object
        # arg1 (bufsize): max amount of data to be recieved at once in bytes, should be a power of 2 like 4096
        # decode turns byte object into readable string
        msg = conn.recv(4096).decode(MSG_FORMAT)
        # msg_length = conn.recv(HEADER).decode(MSG_FORMAT)
        # msg_length = int(msg_length)
        # msg = conn.recv(msg_length).decode(MSG_FORMAT)
        print(f"[{address}] {msg}")


def start():
    server.listen()
    # Server will listen until it crashes or the while loop is exitted
    while True:
        # Accepts connection from client, also blocks execution until a client connects
        # conn -> client socket, address -> (HOST, PORT) of client
        conn, address = server.accept()
        # Creates a new thread once a client has connected
        thread = threading.Thread(target=handle_client, args=(conn, address))
        # Handles the client once started
        thread.start()
        # Returns the number of threads in this python program, 1 is subtracted because a single thread is always running by default
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting....")
start()