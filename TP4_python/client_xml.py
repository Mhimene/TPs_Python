import socket # Permet de communiquer sur le réseau

# Création du client et connexion au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))

print("Connecté au serveur. Tape 'exit' pour quitter.")

# Boucle pour envoyer plusieurs messages (comme un chat)
while True:
    nom = input("Nom : ")
    lieu = input("Lieu : ")
    message_text = input("Message : ")

  # Condition pour quitter proprement
    if message_text == "exit":
        break


# Création du message au format XML
    message = f"""
    <client>
        <type>message</type>
        <nom>{nom}</nom>
        <lieu>{lieu}</lieu>
        <contenu>{message_text}</contenu>
    </client>
    """
# Envoi du message au serveur
    client.send(message.encode())

# Fermeture de la connexion
client.close()