TP6 — Serveur HTTP Python
Exo 1 & 2 — Formater requête / réponse HTTP
python exercice1_requete.py
python exercice2_reponse.py

Lance et regarde le terminal et c'est tout.


Exo 3 — Serveur avec sockets
python exo3.py

Ouvre le navigateur sur : http://localhost:8080/index.html
Pour tester le 404 : http://localhost:8080/nimportequoi


Exo lib — Serveur avec http.server
python exercice_http_server_lib.py

Même chose que l'exo 3 mais plus simple.
http://localhost:8080/index.html


Application Django
1. Installer Django
py -m pip install django
2. Créer le projet
py -m django startproject chatServer
cd chatServer
py manage.py startapp g40aChat
3. fichiers
- g40aChat/views.py 
- g40aChat/urls.py 
- chatServer/urls.py 

4. Ajouter l'app dans settings.py

5. Lancer
py manage.py migrate
py manage.py runserver

6. Tester dans le navigateur
Page d'acceuil : http://127.0.0.1:8000/chat/
Erreur 404  : http://127.0.0.1:8000/nimportequoi/



