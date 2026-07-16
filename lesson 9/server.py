# echo -- server
import socket


HOST: str = "127.0.0.1"     # loopback
PORT: int = 5000


# server_socket = socket.socket( ... )
# socket.AF_INET            -->     IPv4   ( X.X.X.X )
# socket.SOCK_STREAM        -->     TCP
# server_socket -- object of class socket.socket;
with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as server_socket:
    # create SOCKET
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # OK to reuse
    server_socket.bind( ( HOST, PORT ) )
    server_socket.listen()
    print( f"[*] Echo server is listening on {HOST}:{PORT}" )

    # create CONNECTION
    connection, addr = server_socket.accept()
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print( f"[recv] {data!r}" )
            connection.sendall(data)


