# ============================================================
# TP6 - chatServer/settings.py : Configuration du projet
# El Jabri Mejed
# ============================================================

from pathlib import Path

# le repertoire de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# cle secrete du projet (ne jamais la partager en production)
SECRET_KEY = 'django-insecure-tp6-chatserver-key-change-this-in-production'

# DEBUG = False pour que le handler404 fonctionne
# en mode DEBUG Django affiche ses propres pages d'erreur et ignore le notre
DEBUG = False

# j'autorise toutes les adresses a acceder au serveur
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # j'enregistre mon application g40aChat dans le projet
    'g40aChat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# je pointe vers le fichier urls.py principal du projet
# c'est ici que j'indique le nom du module urls -> chatServer.urls (pas chatServer_tp6)
ROOT_URLCONF = 'chatServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chatServer.wsgi.application'

# base de donnees SQLite par defaut
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
