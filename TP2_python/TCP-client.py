import socket
import sys

HOST = '127.0.0.1'
PORT = 5000

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(f'[CLIENT] Connecté au serveur {HOST}:{PORT}')
    print("Tapez vos messages (ou 'quitter' pour terminer) :")

    while True:
        print('[CLIENT] Votre message : ', end='')
        message = sys.stdin.readline().strip()
        s.sendall(message.encode())

        if message.lower() == 'quitter':
            break

        data = s.recv(1024).decode()
        if not data or data.lower() == 'quitter':
            print('[CLIENT] Le serveur a quitté.')
            break
        print(f'[SERVEUR] {data}')

    s.close()

if __name__ == '__main__':
    client()