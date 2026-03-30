import socket  # Permet la communication réseau
import json    # Permet de manipuler le format JSON

# Création du client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur (localhost + port 12345)
client.connect(("localhost", 12345))

print("Connecté au serveur. Tape 'exit' pour quitter.")

# Boucle pour envoyer plusieurs messages
while True:
    nom = input("Nom : ")          # Nom de l'utilisateur
    lieu = input("Lieu : ")        # Lieu de connexion
    message_text = input("Message : ")  # Message à envoyer

    # Si l'utilisateur veut quitter
    if message_text == "exit":
        break

    # Création du message sous forme de dictionnaire Python
    message = {
        "type": "message",         # Type du message (important pour le TP)
        "nom": nom,
        "lieu": lieu,
        "contenu": message_text
    }

    # Transformation en JSON (texte) puis envoi au serveur
    client.send(json.dumps(message).encode())

# Fermeture de la connexion
client.close()