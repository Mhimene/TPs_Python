import socket
import json
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))

nom = input("Ton nom : ")
lieu = input("Ton lieu : ")

# 🔹 Envoi identification
identification = {
    "type": "identification",
    "nom": nom,
    "lieu": lieu
}
client.send(json.dumps(identification).encode())

# 🔹 Fonction pour recevoir les messages
def recevoir():
    while True:
        try:
            data = client.recv(1024)
            if data:
                message = json.loads(data.decode())
                print("\n", message.get("contenu"))
        except:
            break

# Thread pour écouter le serveur
threading.Thread(target=recevoir, daemon=True).start()

print("Tu peux envoyer des messages (exit pour quitter)")

while True:
    msg = input()

    if msg == "exit":
        break

    message = {
        "type": "message",
        "nom": nom,
        "contenu": msg
    }

    client.send(json.dumps(message).encode())

client.close()