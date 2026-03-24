import socket

HOST = '127.0.0.1'
PORT = 1060

# même fonction que côté serveur, on lit exactement "length" octets
def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data)).decode()
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more
    return data

def client():
    # création de la socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))  # on se connecte au serveur
    print('Le serveur a assigne {} comme socket pour le client'.format(s.getsockname()))
    s.sendall('Bonjour !'.encode())  # on envoie notre message
    reply = recv_all(s, 11)  # on attend la réponse "Au revoir !"
    print('Le serveur a repondu : ', repr(reply))
    s.close()

if __name__ == '__main__':
    client()