def listen(self, ip, port):
    # Créer la socket d'écoute
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((ip, port))
    self.server_socket.listen(self.max_gamers)

    # Accepter les connexions jusqu'au maximum autorisé
    while self.nb_connected < self.max_gamers:
        client_socket, address = self.server_socket.accept()
        self.clients.append(client_socket)
        self.nb_connected += 1