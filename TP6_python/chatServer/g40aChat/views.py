# ============================================================
# TP6 - g40aChat/views.py : Les vues de l'application
# El Jabri Mejed
# ============================================================

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# une "vue" en Django c'est une fonction qui recoit une requete HTTP
# et qui retourne une reponse HTTP

def index(request):
    # cette vue est appelee quand l'utilisateur va sur /chat/
    # je retourne la page HTML demandee dans le TP

    page_html = """<!DOCTYPE html>
<html>
<body>

<p>Bonjour et bienvenue </p>
<p style="font-size:50px;">Je sui Melissa et c'est mon premier serveur :) </p>

</body>
</html>"""

    return HttpResponse(page_html)


def page_non_trouvee(request, exception):
    # cette vue est appelee automatiquement quand une URL n'existe pas
    # je retourne une page 404 personnalisee

    page_404 = """<!DOCTYPE html>
<html>
<body>
<h1>404 Not Found</h1>
<p>La page que tu cherches n'existe pas sur ce serveur.</p>
</body>
</html>"""

    # HttpResponseNotFound envoie automatiquement le code 404
    return HttpResponseNotFound(page_404)
