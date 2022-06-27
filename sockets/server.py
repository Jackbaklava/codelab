import socket
import threading # A way of creating multiple threads in a single python program

# Max size of a number of digits
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Automatically gets our local IPv4 adress
# socket.gethostname() -> Returns computer's name
HOST = socket.gethostbyname(socket.gethostname())

# Local IPv4 address from ipconfig
# HOST = "192.168.10.105" (Hard-coded is not good)
# Non-privileged ports are > 1023
PORT = 5050


# Handles communication between class and server, will run concurrently for each client
def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} connected")

    connected = True
    while connected:
        # .recv() Waits to recieve something from client and so also blocks execution, returns a byte object
        # arg1 (bufsize): max amount of data to be recieved at once in bytes, should be a power of 2 like 4096
        # decode turns byte object into readable string (FORMAT)
        # First message sent is the length of the message
        msg_length = conn.recv(HEADER).decode(FORMAT) # "12"
        if msg_length:
            msg_length = int(msg_length) # 12
            # First recv recieves the length, this recieves the msg according to the length
            msg = conn.recv(msg_length).decode(FORMAT) # "Hello World!"
            
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{address}] {msg}")
            conn.send("Message recieved".encode(FORMAT))

    # Closes client connection socket
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on ({HOST}, {PORT})")
    # Server will listen (look for client connections) until it crashes or the while loop is exited
    while True:
        # Accepts connection from client, also blocks execution until a client connects
        # conn -> client socket, address -> (HOST, PORT) of client
        conn, address = server.accept()
        # Creates a new thread once a client has connected, this thread is closed once the target function has been executed
        thread = threading.Thread(target=handle_client, args=(conn, address))
        # Handles the client once started
        thread.start()
        # Returns the number of threads in this python program, 1 is subtracted because a single thread is always running by default
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")



if __name__ == "__main__":
    # Creates a socket
    # 1st arg: family of IP adress (AF_INET is IPv4)
    # 2nd arg: type of socket (SOCK_STREAM uses TCP, allowd two-way comm. and data arrives synchronized)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binds server to address, anything that interacts with this address will interact with the socket 
    server.bind((HOST, PORT))
    print("[STARTING] server is starting....")
    start()