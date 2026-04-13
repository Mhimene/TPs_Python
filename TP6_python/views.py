# g40aChat/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

INDEX_HTML = """<!DOCTYPE html>
<html>
<body>

<p>Bonjour</p>
<p style="font-size:50px;">C'est notre premier serveur</p>

</body>
</html>"""

LOGIN_HTML = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Connexion au Chat</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; margin-top: 80px; }
        .form-box { border: 1px solid #ccc; padding: 30px; border-radius: 8px; width: 320px; }
        h2 { text-align: center; }
        input[type=text], input[type=password] {
            width: 100%; padding: 8px; margin: 8px 0 16px; box-sizing: border-box; border-radius: 4px;
            border: 1px solid #aaa;
        }
        .buttons { display: flex; justify-content: space-between; }
        button { padding: 8px 20px; border: none; border-radius: 4px; cursor: pointer; }
        .btn-connect { background: #007bff; color: white; }
        .btn-cancel  { background: #dc3545; color: white; }
    </style>
</head>
<body>
    <div class="form-box">
        <h2>Connexion au Chat</h2>
        <form method="POST" action="/chat/login/">
            <label>Login :</label>
            <input type="text" name="username" placeholder="Entrez votre login">
            <label>Mot de passe :</label>
            <input type="password" name="password" placeholder="Entrez votre mot de passe">
            <div class="buttons">
                <button type="submit" class="btn-connect">Se connecter</button>
                <button type="reset"  class="btn-cancel">Annuler</button>
            </div>
        </form>
    </div>
</body>
</html>"""

ERROR_404_HTML = """<html>
<body>
<h1>404 Not Found</h1>
<p>La page demandée est introuvable.</p>
</body>
</html>"""


def index(request):
    """Page d'accueil : renvoie le HTML de bienvenue."""
    return HttpResponse(INDEX_HTML, content_type="text/html")


def login_page(request):
    """Page de connexion avec formulaire login / mot de passe."""
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # Authentification basique (à remplacer par une vraie logique)
        if username == "admin" and password == "1234":
            return HttpResponse(f"<h1>Bienvenue, {username} !</h1>")
        else:
            return HttpResponse("<h1>Identifiants incorrects.</h1>", status=401)
    return HttpResponse(LOGIN_HTML, content_type="text/html")


def custom_404(request, exception=None):
    """Vue personnalisée pour les erreurs 404."""
    return HttpResponseNotFound(ERROR_404_HTML, content_type="text/html")
