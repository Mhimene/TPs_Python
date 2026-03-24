import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

clients = {}

def notify_disconnect(name):
    for client_name, client_socket in clients.items():
        try:
            client_socket.send(f"{name} s'est déconnecté".encode())
        except:
            pass

def handle_client(client_socket, name):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            dest, msg = message.split("|", 1)

            if dest in clients:
                clients[dest].send(f"{name}: {msg}".encode())

        except:
            break

    if name in clients:
        del clients[name]

    notify_disconnect(name)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Serveur en écoute...")

    while True:
        client_socket, addr = server.accept()

        name = client_socket.recv(1024).decode()
        clients[name] = client_socket

        client_socket.send(("Clients connectés: " + ", ".join(clients.keys())).encode())

        thread = threading.Thread(target=handle_client, args=(client_socket, name))
        thread.start()

start_server()