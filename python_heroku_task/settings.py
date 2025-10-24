import os
import dj_database_url
from pathlib import Path

# ... (existing code)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-fallback-secret-key-change-this')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER_ON_RAILWAY' not in os.environ and 'RUN_ON_REPLIT' not in os.environ  # Or set to False

ALLOWED_HOSTS = ['*']  # For Heroku; restrict later with your app's domain

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',  # Local fallback
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where collectstatic puts files

# Add WhiteNoise to middleware (after SecurityMiddleware, before CommonMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]

# Static files storage for WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'