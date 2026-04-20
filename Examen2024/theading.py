import threading

def run(self):
    """Fonction principale du serveur Game"""
    self.listen("0.0.0.0", 5000)

    # Lancer un thread par joueur connecté
    threads = []
    for client_id in range(len(self.clients)):
        t = threading.Thread(
            target=self.communicate_with_client,
            args=(client_id,)
        )
        threads.append(t)
        t.start()

    # Attendre la fin de tous les threads
    for t in threads:
        t.join()