class Game(object):
    def __init__(self, max_gamers, nbr_sticks) -> None:
        """
        max_gamers : le nombre maximal de joueurs
        nbr_sticks : nombre de bâtons dans le jeux
        """
        self.max_gamers = max_gamers
        self.nbr_sticks = nbr_sticks
        self.clients = []        # liste des sockets clients connectés
        self.nb_connected = 0   # compteur de joueurs connectés