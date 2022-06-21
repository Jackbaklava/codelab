[Tutorial I followed](https://youtu.be/3QiPPX-KeSc)

# Client-Server Model
- Server(s) handle the logic and communication between the clients and so they remove the need to connect to other clients, which means they are faster
- Clients are the end-user and connect to the server(s)

# Sockets
- A socket is an endpoint of a two way communication link between two programs running on a network.
- Each socket has an address and is created at each end of communication.

![image](https://media.geeksforgeeks.org/wp-content/uploads/20200509144309/1406-4.png)

# FIN_WAIT_2
If many sockets which were connected to a specific remote application end up stuck in this state, it usually indicates that the remote application either always dies unexpectedly when in the CLOSE_WAIT state or just fails to perform an active close after the passive close.

The timeout for sockets in the FIN-WAIT-2 state is defined with the parameter tcp_fin_timeout. You should set it to value high enough so that if the remote end-point is going to perform an active close, it will have time to do it. On the other hand sockets in this state do use some memory (even though not much) and this could lead to a memory overflow if too many sockets are stuck in this state for too long.

`netstat -an` to show current socket state

[Commmon Errors](https://realpython.com/python-sockets/#errors)


