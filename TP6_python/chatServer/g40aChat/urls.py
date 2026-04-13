# ============================================================
# TP6 - g40aChat/urls.py : URLs de l'application g40aChat
# El Jabri Mejed
# ============================================================

from django.urls import path
from . import views

# urlpatterns c'est la liste de toutes les URLs gerees par cette application
# chaque path() lie une URL a une vue
urlpatterns = [
    # quand l'utilisateur va sur /chat/ (chaine vide car le prefixe "chat/"
    # est deja defini dans le fichier urls.py principal)
    # Django appelle la fonction index de views.py
    path('', views.index, name='index'),
]
