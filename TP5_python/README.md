--> Ce que j'ai corrigé
1. La fonction checksum manquait
Elle n'était pas définie dans le code de base alors qu'elle était utilisée. Je l'ai ajoutée, elle sert à vérifier l'intégrité du paquet.
2. ip_ihl_ver était inversé
La version IP doit être sur les 4 bits de poids fort donc la formule correcte est :
pythonip_ihl_ver = (ip_version << 4) + ip_ihl
3. La signature de create_tcp_header était fausse
L'ancienne version prenait ip_header et tcp_header en paramètres avant même qu'ils soient créés. J'ai simplifié à :
pythondef create_tcp_header(message, ip_source, ip_dest)
4. Le checksum TCP était mal calculé
Il faut le calculer sur pseudo_header + tcp_header + message, pas seulement sur le pseudo_header.
5. Le message n'était pas converti en bytes
Un str Python ne peut pas être concaténé avec des bytes, j'ai ajouté un .encode().
Lancer le code
bash python raw_socket.py

Important ; Nécessite un terminal en administrateur sur Windows.

6. Raw socket vs Socket normale
Une socket normale se place à la couche 4 du modèle OSI, c'est-à-dire la couche Transport. Le système gère automatiquement tout ce qui est entête IP et TCP, on a juste à envoyer les données. C'est simple à utiliser et ça ne nécessite aucun droit particulier.
Une raw socket se place à la couche 3, la couche Réseau. On doit construire soi-même les entêtes IP et TCP à la main avant d'envoyer quoi que ce soit. C'est beaucoup plus bas niveau et ça demande des droits administrateur. En contrepartie on a un contrôle total sur le paquet, ce qui est utile pour faire de l'analyse réseau ou tester des protocoles.

7. Limites des raw sockets

--> Droits admin obligatoires : impossible de les utiliser sans être administrateur, ce qui les rend inutilisables dans un contexte normal.
--> Pas adaptées aux vraies applications : elles servent surtout à faire de l'analyse réseau ou des tests bas niveau, pas à faire une vraie application client/serveur.
--> Complexité : on doit gérer soi-même des choses que le système fait normalement tout seul (checksum, numéros de séquence, flags TCP...).
--> Maintenance difficile : le moindre champ mal rempli dans l'entête et le paquet est rejeté sans message d'erreur clair.