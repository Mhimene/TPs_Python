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
bashpython tp5_raw_socket.py

Important ; Nécessite un terminal en administrateur sur Windows.