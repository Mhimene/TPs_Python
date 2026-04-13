# ============================================================
# TP6 - chatServer/urls.py : URLs principales du projet
# El Jabri Mejed
# ============================================================

from django.contrib import admin
from django.urls import path, include

# je dis a Django quoi faire quand une URL n'existe pas
# il appellera ma vue page_non_trouvee dans g40aChat/views.py
handler404 = 'g40aChat.views.page_non_trouvee'

urlpatterns = [
    # l'url admin/ pointe vers la console d'administration Django
    path('admin/', admin.site.urls),

    # toutes les URLs qui commencent par "chat/" sont gerees par g40aChat/urls.py
    # donc quand l'utilisateur va sur /chat/, Django cherche dans g40aChat/urls.py
    path('chat/', include('g40aChat.urls')),
]
