import socket
import threading

class LeChat:
    def __init__(self, max_client, max_message_len, ip_address, port):
        self.max_client = max_client
        self.max_message_len = max_message_len
        self.ip_address = ip_address
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip_address, self.port))

        self.clients = []
        self.current_clients = 0

        # pour évaluation
        self.total_score = 0
        self.nb_scores = 0


    # gestion connexions TCP
    def manage_connexions(self):
        self.server_socket.listen(self.max_client)
        print("Serveur en attente...")

        while self.current_clients < self.max_client:
            client_socket, addr = self.server_socket.accept()
            print(f"Client connecté: {addr}")

            self.clients.append(client_socket)
            self.current_clients += 1

            t = threading.Thread(target=self.handle_client, args=(client_socket,))
            t.start()

    # tokenizer
    def tokenizer(self, message, vocab):
        words = message.split()

        for w in words:
            if w in vocab:
                tokens.append(vocab[w])

        return tokens


    # simulation LLM
    def handle_llm(self, tokens):
        return f"Réponse générée pour {tokens}"


    # communication client
    def handle_client(self, client):
        vocab = {"bonjour": 1, "comment": 2, "ça": 3, "va": 4}

        while True:
            msg = client.recv(1024).decode()

            # vérification
            if (not msg.endswith("?") or 
                len(msg) > self.max_message_len or 
                "merci" in msg.lower()):
                
                client.send("Texte invalide".encode())
                continue

            # tokenizer + LLM
            tokens = self.tokenizer(msg, vocab)
            response = self.handle_llm(tokens)

            client.send(response.encode())

            # recevoir note
            note = client.recv(1024).decode()

            if note.isdigit():
                note = int(note)
                if 0 <= note <= 10:
                    self.total_score += note
                    self.nb_scores += 1


    # moyenne
    def get_evaluation(self):
        if self.nb_scores == 0:
            return 0
        return self.total_score / self.nb_scores


    # lancement serveur
    def start(self):
        self.manage_connexions()


# main
if __name__ == "__main__":
    server = LeChat(max_client=2, max_message_len=100, ip_address="localhost", port=12345)
    server.start()