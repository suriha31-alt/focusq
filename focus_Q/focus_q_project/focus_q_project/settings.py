import os
from pathlib import Path

# -------- BASE DIRECTORY --------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------- SECURITY --------
SECRET_KEY = 'your-secret-key'
DEBUG = True

ALLOWED_HOSTS = []

# -------- INSTALLED APPS --------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'analysis',   # your app
]

# -------- MIDDLEWARE --------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------- URL CONFIG --------
ROOT_URLCONF = 'focus_q_project.urls'

# -------- TEMPLATES --------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],   # you can add custom template path later
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -------- DATABASE --------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------- STATIC FILES --------
STATIC_URL = '/static/'

# -------- MEDIA FILES (VERY IMPORTANT FOR GRAPHS) --------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')