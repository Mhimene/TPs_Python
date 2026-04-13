# ============================================================
# EXERCICE 1 - Client météo avec OpenWeatherMap API

# Ce programme demande à l'utilisateur d'entrer le nom d'une
# ville, puis appelle l'API REST de openweathermap.org pour
# afficher la météo actuelle de cette ville.


import requests  # on utilise la lib requests pour faire des appels HTTP

# clé API (à récupérer sur https://openweathermap.org après création de compte) ---
API_KEY = "8507643485cdb29dd05be53c5219559d"

# On demande à l'utilisateur d'entrer une ville
ville = input("Entre le nom d'une ville : ")

# On construit l'URL de l'API avec les paramètres
# - q     : nom de la ville
# - appid : ta clé API
# - units : "metric" pour avoir les températures en °C
# - lang  : "fr" pour avoir la description en français
url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}&units=metric&lang=fr"

# On fait un GET HTTP vers l'API (comme taper l'URL dans un navigateur)
response = requests.get(url)

# On vérifie si la requête a bien marché (code 200 = OK)
if response.status_code == 200:
    # On récupère la réponse en JSON (c'est un dictionnaire Python)
    data = response.json()

    # On extrait les infos qui nous intéressent
    nom_ville     = data["name"]
    pays          = data["sys"]["country"]
    temperature   = data["main"]["temp"]
    ressenti      = data["main"]["feels_like"]
    description   = data["weather"][0]["description"]
    humidite      = data["main"]["humidity"]
    vent          = data["wind"]["speed"]

    # On affiche joliment les résultats
    print(f"\n🌍 Météo à {nom_ville} ({pays})")
    print(f"🌡️  Température : {temperature}°C (ressenti {ressenti}°C)")
    print(f"🌤️  Conditions  : {description}")
    print(f"💧 Humidité    : {humidite}%")
    print(f"💨 Vent        : {vent} m/s")

elif response.status_code == 404:
    # La ville n'a pas été trouvée
    print(f"❌ Ville '{ville}' introuvable. Vérifie l'orthographe.")
else:
    # Autre erreur (clé API invalide, etc.)
    print(f"❌ Erreur {response.status_code} : {response.text}")


# ============================================================
# COMMENT TESTER :
# 1. Crée un compte sur https://openweathermap.org
# 2. Va dans "API Keys" et copie ta clé
# 3. Remplace "API_Key" par ta vraie clé
# 4. Installe requests si besoin : pip install requests
# 5. Lance : python exo1_meteo.py
# 6. Tape le nom d'une ville ex: "Paris" ou "London"
# ============================================================