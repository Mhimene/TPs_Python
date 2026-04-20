import socket
import threading

class Game:
    def __init__(self, max_gamers, nbr_sticks):
        self.max_gamers = max_gamers
        self.nbr_sticks = nbr_sticks

        self.players = []
        self.sockets = []
        self.current_players = 0

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("localhost", 12345))


    # Fonction pour écouter les connexions
    def listen(self):
        self.server_socket.listen(self.max_gamers)

        print("Serveur en attente de connexions...")

        while self.current_players < self.max_gamers:
            client_socket, addr = self.server_socket.accept()
            print(f"Connexion de {addr}")

            self.sockets.append(client_socket)
            self.current_players += 1


    # Fonction pour envoyer un message
    def send(self, client, message):
        client.send(message.encode())


    # Fonction pour lire un message
    def read(self, client):
        return client.recv(1024).decode()


    # Communication avec un client
    def communicate_with_client(self, client):
        while True:
            # envoyer nb de bâtons
            self.send(client, f"Il reste {self.nbr_sticks} bâtonnets")
            self.send(client, "Choisissez 1, 2 ou 3 bâtonnets à retirer")

            msg = self.read(client)

            # Vérification
            if not msg.isdigit():
                self.send(client, "Erreur")
                continue

            choix = int(msg)

            if choix < 1 or choix > 3:
                self.send(client, "Erreur")
                continue

            # Mise à jour
            self.nbr_sticks -= choix

            if self.nbr_sticks > 0:
                self.send(client, "vous restez dans le jeu")
            else:
                self.send(client, "perdu")

                # autres gagnent
                for c in self.sockets:
                    if c != client:
                        self.send(c, "gagné")
                break


    # Fonction principale
    def start(self):
        self.listen()

        threads = []

        for client in self.sockets:
            t = threading.Thread(target=self.communicate_with_client, args=(client,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()


# Lancement du serveur
if __name__ == "__main__":
    game = Game(max_gamers=2, nbr_sticks=10)
    game.start()