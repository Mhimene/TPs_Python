import socket  # Communication réseau
import json    # Lecture et écriture JSON

# Création du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 🔥 Permet de relancer le serveur sans erreur de port
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Association adresse + port
server.bind(("localhost", 12345))

# Mise en écoute
server.listen(5)

print("Serveur JSON en attente...")

# Boucle infinie pour accepter plusieurs clients
while True:
    client_socket, addr = server.accept()  # Connexion d’un client
    print("Client connecté :", addr)

    # Boucle pour recevoir plusieurs messages
    while True:
        data = client_socket.recv(1024)

        # Si le client se déconnecte
        if not data:
            print("Client déconnecté")
            break

        try:
            # Transformation JSON → dictionnaire Python
            message = json.loads(data.decode())

            # Récupération des informations
            nom = message.get("nom")
            lieu = message.get("lieu")
            contenu = message.get("contenu")

            # Affichage du message
            if contenu:
                print(f"{nom} ({lieu}) : {contenu}")
            else:
                print(f"{nom} connecté depuis {lieu}")

        except Exception as e:
            # Si erreur dans le format JSON
            print("Erreur JSON :", e)

    # Fermeture de la connexion client
    client_socket.close()