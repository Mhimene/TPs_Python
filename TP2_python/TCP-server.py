import socket
import sys

HOST = '127.0.0.1'
PORT = 5000

def server():
    # on crée une socket TCP, plus fiable qu'UDP pour un chat
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # on attache le serveur à l'adresse et au port
    s.bind((HOST, PORT))

    # on attend qu'un client arrive
    s.listen(1)
    print(f'[SERVEUR] En attente de connexion sur {HOST}:{PORT}...')

    # dès qu'un client se connecte, on l'accepte
    conn, addr = s.accept()
    print(f'[SERVEUR] Client connecté : {addr}')

    # boucle de chat : on échange des messages jusqu'à ce que quelqu'un tape "quitter"
    while True:

        # on reçoit le message du client
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'quitter':
            print('[SERVEUR] Le client a quitté.')
            break
        print(f'[CLIENT] {data}')

        # le serveur tape sa réponse
        print('[SERVEUR] Votre réponse : ', end='')
        reponse = sys.stdin.readline().strip()
        conn.sendall(reponse.encode())

        if reponse.lower() == 'quitter':
            break

    conn.close()
    s.close()

if __name__ == '__main__':
    server()