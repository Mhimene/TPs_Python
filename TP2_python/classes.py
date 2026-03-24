import socket
import sys

HOST = '127.0.0.1'
PORT = 1060

# classe de base commune aux deux — c'est ici qu'on met ce qui est partagé
class SocketBase:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def recv_all(self, sock, length):
        data = ''
        while len(data) < length:
            more = sock.recv(length - len(data)).decode()
            if not more:
                raise EOFError('la socket a ete fermee')
            data += more
        return data

    # méthode abstraite : chaque sous-classe doit l'implémenter à sa façon (polymorphisme)
    def run(self):
        raise NotImplementedError("Implémenter run() dans la sous-classe")

    def close(self):
        self.sock.close()


class Server(SocketBase):
    def run(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print('Serveur en écoute sur', self.sock.getsockname())
        sc, sockname = self.sock.accept()
        print('Connexion acceptée de', sockname)
        message = self.recv_all(sc, 9)
        print('Message reçu :', repr(message))
        sc.sendall('Au revoir !'.encode())
        sc.close()


class Client(SocketBase):
    def run(self):
        self.sock.connect((self.host, self.port))
        print('Connecté via', self.sock.getsockname())
        self.sock.sendall('Bonjour !'.encode())
        reply = self.recv_all(self.sock, 11)
        print('Serveur a répondu :', repr(reply))
        self.sock.close()


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == 'server':
        app = Server(HOST, PORT)
    else:
        app = Client(HOST, PORT)

    # polymorphisme en action : même appel run() pour les deux
    app.run()