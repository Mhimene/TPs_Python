import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

def receive(client):
    while True:
        try:
            print(client.recv(1024).decode())
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Nom: ")
client.send(name.encode())

thread = threading.Thread(target=receive,args=(client,))
thread.start()

while True:
    dest = input("Destinataire: ")
    msg = input("Message: ")

    client.send(f"{dest}|{msg}".encode())