import socket


HOST: str = "127.0.0.1"
PORT: int = 5000


with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b"HELLO WORLD!!!")          # b"" -->  text --> byte

    data = client_socket.recv(1024)
    print(f"[client received] {data!r}")
