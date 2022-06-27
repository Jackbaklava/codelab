import socket
import server


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connects to the server socket
client.connect((server.HOST, server.PORT))


def send(msg):
    # We need to encode data into bytes format before sending
    # .encode() turns from arg_format into bytes object
    message = msg.encode(server.FORMAT) # b"Hello World!"
    msg_length = len(message) # 12
    send_length = str(msg_length).encode(server.FORMAT) # b"12"
    # Pads it so that length matches the HEADER int
    send_length += b' ' * (server.HEADER - len(send_length)) # b"12..."
    # Both arguments are combined and sent to the server, the server decides with the arg of .recv() to decide how much data to recieve at once. So, we have to pad send_length so that its the first thing recieved
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(server.FORMAT))


send("Hello World!")
# execution stops because this is the end of the file eventhough the socket is still connected with the server
# See FIN_WAIT_2 in notes.md

send(server.DISCONNECT_MESSAGE)