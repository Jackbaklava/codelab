import socket

HOST = "127.0.0.1" #localhost
PORT = 65432 # >1023

# Creates socket
# AF_INET = ipv4
# sock stream is type of socket where it uses TCP and data arrives synchronized
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Binds created socket to a port
    s.bind((HOST, PORT))
    # Socket now listens for any connections
    s.listen()
    # .accept blocks execution
    conn, addr = s.accept()
    #conn is the client socket object, addr is the address of the client socket
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)