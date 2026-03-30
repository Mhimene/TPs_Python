import socket  # Communication réseau
import xml.etree.ElementTree as ET  # Pour lire le XML

# Création du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))  # Adresse + port
server.listen(5)  # Le serveur attend des connexions

print("Serveur XML en attente...")

# Boucle infinie pour accepter plusieurs clients
while True:
    client_socket, addr = server.accept()  # Connexion d’un client
    print("Client connecté :", addr)

    # Boucle pour recevoir plusieurs messages du même client
    while True:
        data = client_socket.recv(1024)  # Réception des données

        # Si plus de données → client déconnecté
        if not data:
            print("Client déconnecté")
            break

        try:
            # Transformation du texte XML en structure exploitable
            root = ET.fromstring(data.decode())

            # Récupération des informations du message
            nom = root.find("nom").text
            lieu = root.find("lieu").text
            contenu = root.find("contenu")

            # Si c’est un message → on affiche le contenu
            if contenu is not None:
                print(f"{nom} ({lieu}) : {contenu.text}")
            else:
                # Sinon c’est juste une connexion
                print(f"{nom} connecté depuis {lieu}")

        except Exception as e:
            # Gestion des erreurs si le XML est mal formé
            print("Erreur XML :", e)

    # Fermeture du client
    client_socket.close()