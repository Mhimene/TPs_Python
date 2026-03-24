import socket

HOST = '127.0.0.1'
PORT = 1060

# on lit exactement "length" caractères depuis la socket
def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data)).decode()
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more
    return data

def server():
    # création de la socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # évite "port déjà utilisé"
    s.bind((HOST, PORT))
    s.listen(1)  # on se met en attente d'un client

    while True:
        print('le serveur ecoute a cette adresse :', s.getsockname())
        sc, sockname = s.accept()  # on accepte la connexion entrante
        print('Le serveur a accepte une connection de ', sockname)
        message = recv_all(sc, 9)  # on lit les 9 octets de "Bonjour !"
        print('Les 9 octets recu : ', repr(message))
        sc.sendall('Au revoir !'.encode())  # on répond au client
        sc.close()
        print("Une reponse a ete envoye, la socket est fermee")

if __name__ == '__main__':
    server()