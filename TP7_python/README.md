# TP7 – APIs REST avec Python et Django

## Objectif du TP

L’objectif de ce TP est de comprendre le fonctionnement des APIs REST, d’apprendre à utiliser des outils comme HTTPie et Postman, et de créer une API REST avec Django permettant de gérer des messages et des utilisateurs.

---

## 1. Test HTTP avec HTTPie

Nous avons utilisé HTTPie pour envoyer des requêtes HTTP.

### Commande utilisée :

```bash
python -m httpie --body GET www.google.com > page.html
```

### Résultat :

* Récupération du contenu HTML d’une page web
* Sauvegarde dans un fichier `page.html`
* Ouverture du fichier dans un navigateur

---

## 2. API météo (OpenWeather)

Nous avons utilisé une API publique pour récupérer la météo.

### Fonctionnement :

* Envoi d’une requête HTTP vers l’API OpenWeather
* Réception des données au format JSON
* Affichage de la température et de la météo

### Exemple de résultat :

* Ville : Paris
* Température : 18°C
* Description : nuageux

---

## 3. Création du projet Django

### Installation :

```bash
python -m pip install django
```

### Création du projet :

```bash
python -m django startproject monprojet
cd monprojet
```

### Création de l’application :

```bash
python manage.py startapp myapi
```

### Configuration :

Ajout de l’application dans `settings.py` :

```python
'myapi.apps.MyapiConfig',
```

---

## 4. Base de données et admin

### Migration :

```bash
python manage.py migrate
```

### Création d’un administrateur :

```bash
python manage.py createsuperuser
```

### Lancement du serveur :

```bash
python manage.py runserver
```

Accès à :

```
http://127.0.0.1:8000/admin
```

---

## 5. Modèle Message

Création d’un modèle pour représenter les messages :

```python
class Message(models.Model):
    source = models.CharField(max_length=60)
    to = models.CharField(max_length=60)
    body = models.TextField()
```

Ajout dans l’interface d’administration pour gérer les messages.

---

## 6. Django REST Framework

### Installation :

```bash
python -m pip install djangorestframework
```

Ajout dans `settings.py` :

```python
'rest_framework',
```

---

## 7. Création de l’API Message

Un serializer est utilisé pour convertir les objets Message en JSON.

Une vue est définie pour gérer les opérations CRUD (GET, POST, PUT, DELETE).

Une URL est configurée pour accéder à l’API :

```
http://127.0.0.1:8000/messages
```

### Résultat :

* Liste des messages en JSON
* Possibilité d’ajouter et modifier des messages

---

## 8. API des utilisateurs

La même logique est appliquée pour les utilisateurs en utilisant le modèle User de Django.

URL d’accès :

```
http://127.0.0.1:8000/users
```

### Résultat :

* Liste des utilisateurs
* Données au format JSON

---

## 9. Fusion de deux tableaux

### Objectif :

Fusionner deux tableaux triés.

### Exemple :

* Entrée : [1, 2, 3] et [2, 5, 6]
* Sortie : [1, 2, 2, 3, 5, 6]

### Principe :

Comparer les éléments des deux tableaux et ajouter le plus petit dans le tableau résultat afin de conserver l’ordre.

---

## Conclusion

Ce TP a permis de comprendre le fonctionnement des APIs REST, d’utiliser des outils HTTP, de consommer une API externe et de créer une API REST avec Django en manipulant des données au format JSON.
