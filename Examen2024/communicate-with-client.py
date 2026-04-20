def communicate_with_client(self, client_id: int) -> None:
    # Envoyer la demande au joueur
    send(client_id, "Choisissez 1, 2 ou 3 bâtonnets à retirer")

    # Lire la réponse
    response = read()

    # Vérifier que la réponse est valide
    if not response.isdigit():
        send(client_id, "Erreur: veuillez entrer un chiffre valide")
        return

    choix = int(response)

    if choix < 1 or choix > 3:
        send(client_id, "Erreur: le choix doit être entre 1 et 3")
        return

    # Appliquer le choix
    self.nbr_sticks -= choix

    # Vérifier s'il reste des bâtonnets
    if self.nbr_sticks > 0:
        send(client_id, "vous restez dans le jeu")
    else:
        # Ce joueur a pris le dernier bâtonnet → il perd
        send(client_id, "perdu")
        # Envoyer "gagné" à tous les autres joueurs
        for i, client in enumerate(self.clients):
            if i != client_id:
                send(i, "gagné")