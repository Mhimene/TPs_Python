# Réponses aux questions du TP2

---

## 1. Polymorphisme

Oui on peut l'utiliser ici. On a une classe de base `SocketBase` avec une méthode `run()` non implémentée. Les classes `Server` et `Client` héritent de cette classe et chacune redéfinit `run()` à sa façon.

```python
class SocketBase:
    def run(self):
        raise NotImplementedError("à implémenter dans la sous-classe")

class Server(SocketBase):
    def run(self):
        # logique du serveur

class Client(SocketBase):
    def run(self):
        # logique du client
```

On appelle toujours `app.run()` de la même manière, mais Python sait quoi faire selon si c'est un `Server` ou un `Client`. C'est ça le polymorphisme.

---

## 2. UDP ou TCP pour le chat ?

**TCP est mieux adapté pour une application de chat.**

En UDP les paquets peuvent arriver dans le désordre ou se perdre complètement, sans que personne ne le sache. Pour un chat c'est un problème — imaginer recevoir les messages dans le mauvais ordre ou ne pas les recevoir du tout.

TCP garantit que chaque message arrive, dans le bon ordre. C'est exactement ce qu'on veut pour une conversation. UDP c'est bien pour du streaming ou des jeux où la vitesse prime, mais pas pour un chat.

---

## 3. Doublons

On convertit le tableau en `set`. Un set supprime automatiquement les doublons, donc si la taille change c'est qu'il y en avait.

```python
def contient_doublon(t):
    return len(t) != len(set(t))

contient_doublon([1, 2, 3, 1])  # True
contient_doublon([1, 2, 3, 4])  # False
```

---

## 4. Anagrammes

On trie les lettres des deux mots et on compare. Si c'est identique, ils utilisent les mêmes lettres donc c'est un anagramme.

```python
def est_anagramme(s, t):
    return sorted(s.lower()) == sorted(t.lower())

est_anagramme("python", "onhtyp")  # True
est_anagramme("tp", "tps")         # False
```
