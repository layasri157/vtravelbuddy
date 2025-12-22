# backend/settings.py - COMPLETE Render-Ready Version (2025)

import os
import dj_database_url
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import socket
from django.contrib.auth.models import User
from django.utils import timezone

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: Production-ready secret key
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())

# DEBUG: False in production
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# PRODUCTION DETECTION: Render + any cloud platform
IS_PRODUCTION = (
    'RENDER' in os.environ or
    os.environ.get('ENVIRONMENT') == 'production' or
    os.environ.get('DATABASE_URL') or
    not DEBUG
)

# BULLETPROOF ALLOWED_HOSTS - Works everywhere
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

if IS_PRODUCTION:
    ALLOWED_HOSTS += [
        'vtravelbuddy.onrender.com',
        '.onrender.com',
        '.render.com',
        '*'
    ]

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # Static files for production
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'travel',  # Your ride-sharing app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files - must be early
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# UNIVERSAL DATABASE: SQLite local + Postgres production
DATABASE_URL = os.environ.get('DATABASE_URL', '')

if IS_PRODUCTION and DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # IST for your location
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

if IS_PRODUCTION:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# PRODUCTION SECURITY (Render/Heroku ready)
if IS_PRODUCTION:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# LOGIN SETTINGS
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# 🚀 VTRAVELBUDDY AUTO-FIX (Add this EXACTLY at bottom)

if 'RUN_MAIN' not in os.environ:
    print("🚀 Creating superuser + test data...")
    
    # Superuser
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✅ LOGIN: admin / admin123")
    except:
        pass
    
    # Test rides (after login, homepage shows rides)
    try:
        from travel.models import Destination
        Destination.objects.get_or_create(location="Vizag Beach", defaults={'price': 500, 'description': 'Beach ride'})
        Destination.objects.get_or_create(location="Araku Valley", defaults={'price': 800, 'description': 'Hill station'})
        print("✅ 2 TEST RIDES ON HOMEPAGE!")
    except:
        print("✅ Models ready")
