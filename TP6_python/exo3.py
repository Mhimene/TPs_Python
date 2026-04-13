import socket
import threading
 
 
# je definis la page HTML renvoyee quand l'utilisateur demande index.html
PAGE_INDEX = """<!DOCTYPE html>
<html>
<body>
 
<p>Hello Hello</p>
<p style="font-size:50px;">Je m'appelle Melissa et c'est mon premier serveur</p>
<p>A bientot !</p>
</body>
</html>"""
 
# page d'erreur renvoyee quand la requete est mauvaise
PAGE_404 = """<!DOCTYPE html>
<html>
<body>
<h1>404 Not Found</h1>
<p>La page demandee n'existe pas.</p>
</body>
</html>"""
 
 
def formater_reponse_http(status_code, status_message, body):
    # je construis la reponse HTTP manuellement comme en exercice 2
    reponse = f"HTTP/1.1 {status_code} {status_message}\r\n"
    reponse += "Server: PythonTPServer\r\n"
    reponse += "Content-Type: text/html\r\n"
    reponse += "Connection: Closed\r\n"
    reponse += "\r\n"  # ligne vide obligatoire
    reponse += body
    return reponse
 
 
def gerer_client(connexion, adresse):
    # cette fonction s'occupe d'un seul client a la fois
    print(f"Nouvelle connexion de : {adresse}")
 
    try:
        # je recois les donnees envoyees par le client (max 4096 octets)
        donnees = connexion.recv(4096).decode("utf-8")
 
        if not donnees:
            connexion.close()
            return
 
        # je recupere la premiere ligne de la requete HTTP
        # exemple : "GET /index.html HTTP/1.1"
        premiere_ligne = donnees.split("\r\n")[0]
        print(f"Requête reçue : {premiere_ligne}")
 
        # je decoupe pour extraire la methode et l'url
        parties = premiere_ligne.split(" ")
 
        # je verifie que c'est bien un GET vers /index.html
        if len(parties) == 3 and parties[0] == "GET" and parties[1] == "/index.html":
            # bonne requete -> je renvoie la page avec 200 OK
            reponse = formater_reponse_http(200, "OK", PAGE_INDEX)
        else:
            # mauvaise requete -> je renvoie une erreur 404
            reponse = formater_reponse_http(404, "Not Found", PAGE_404)
 
        # j'envoie la reponse au client
        connexion.sendall(reponse.encode("utf-8"))
 
    except Exception as e:
        print(f"Erreur avec le client {adresse} : {e}")
 
    finally:
        # je ferme toujours la connexion a la fin
        connexion.close()
        print(f"Connexion fermée avec : {adresse}")
 
 
def lancer_serveur(port=8080):
    # je cree un socket TCP
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    # j'active l'option pour reutiliser le port rapidement apres un arret
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
    # je lie le serveur a toutes les interfaces reseau sur le port choisi
    serveur.bind(("", port))
 
    # le serveur commence a ecouter les connexions entrantes
    serveur.listen(5)
    print(f"Serveur démarré sur le port {port}")
    print(f"Ouvre ton navigateur sur : http://localhost:{port}/index.html")
    print("Appuie sur Ctrl+C pour arrêter le serveur\n")
 
    try:
        while True:
            # j'attends qu'un client se connecte
            connexion, adresse = serveur.accept()
 
            # je cree un thread pour chaque client pour ne pas bloquer les autres
            thread = threading.Thread(target=gerer_client, args=(connexion, adresse))
            thread.daemon = True
            thread.start()
 
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
    finally:
        serveur.close()
 
 
# ============================================================
# LANCEMENT
# ============================================================
 
if __name__ == "__main__":
    lancer_serveur(port=8080)