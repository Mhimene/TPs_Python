TP6 — Serveur HTTP Python
Exo 1 & 2 — Formater requête / réponse HTTP
python exercice1_requete.py
python exercice2_reponse.py

Lance et regarde le terminal, c'est tout.


Exo 3 — Serveur avec sockets
python exercice3_serveur_socket.py

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
3. Copier les fichiers

g40aChat/views.py → coller le code des vues
g40aChat/urls.py → créer le fichier et coller le code
chatServer/urls.py → remplacer par le code fourni

4. Ajouter l'app dans settings.py
Ouvrir chatServer/settings.py et ajouter dans INSTALLED_APPS :
python'g40aChat',
5. Lancer
py manage.py migrate
py manage.py runserver
6. Tester dans le navigateur
URLRésultathttp://127.0.0.1:8000/chat/Page d'accueilhttp://127.0.0.1:8000/chat/login/Formulaire loginhttp://127.0.0.1:8000/nimportequoi/Page 404

Login : admin / Mot de passe : 1234


Problèmes fréquents
ErreurSolutionpip not recognizedUtiliser py -m pip à la placedjango-admin not recognizedUtiliser py -m django à la placePage 404 sur /chat/Vérifier chatServer/urls.py et g40aChat/urls.pyviews.py videColler le code des vues dedans