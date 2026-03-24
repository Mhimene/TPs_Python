import socket
import argparse
import sys

HOST = '127.0.0.1'
PORT = 1060

def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data)).decode()
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more
    return data

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print('Serveur en écoute sur', s.getsockname())
    sc, sockname = s.accept()
    print('Connexion acceptée de', sockname)
    message = sc.recv(1024).decode()
    print('Message reçu :', repr(message))
    sc.sendall('Au revoir !'.encode())
    sc.close()

def client(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(message.encode())
    reply = s.recv(1024).decode()
    print('Serveur a répondu :', repr(reply))
    s.close()

if __name__ == '__main__':
    # argparse gère les arguments passés en ligne de commande
    parser = argparse.ArgumentParser(description='TCP Client/Serveur en un seul fichier')
    parser.add_argument('mode', choices=['server', 'client'], help='Mode de lancement')
    parser.add_argument('-p', '--port', type=int, default=PORT, help='Port à utiliser')
    args = parser.parse_args()

    PORT = args.port

    if args.mode == 'server':
        server()
    else:
        # sys.stdin permet à l'utilisateur de taper son propre message
        print("Entrer le message à envoyer : ", end='')
        message = sys.stdin.readline().strip()
        client(message)