import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost", 12345))
server.listen(5)

print("Serveur chat en attente...")

clients = []  # liste des clients connectés

while True:
    client_socket, addr = server.accept()
    print("Client connecté :", addr)

    clients.append(client_socket)

    while True:
        data = client_socket.recv(1024)

        if not data:
            print("Client déconnecté")
            clients.remove(client_socket)
            break

        try:
            message = json.loads(data.decode())
            type_msg = message.get("type")

            # 🔹 Identification
            if type_msg == "identification":
                print(f"{message['nom']} connecté depuis {message['lieu']}")

            # 🔹 Message chat
            elif type_msg == "message":
                texte = f"{message['nom']} : {message['contenu']}"
                print(texte)

                # envoyer à tous les clients
                for c in clients:
                    c.send(json.dumps({
                        "type": "message",
                        "contenu": texte
                    }).encode())

            # 🔹 Etat
            elif type_msg == "etat":
                print(f"{message['nom']} est {message['status']}")

            # 🔹 Notification
            elif type_msg == "notification":
                print(f"Notification : {message['contenu']}")

        except:
            print("Erreur JSON")

    client_socket.close()