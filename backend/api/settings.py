import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = bool(os.getenv("DJANGO_DEBUG"))

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]

INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS = [
    "corsheaders",
    "debug_toolbar",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "drfpasswordless",
    "drf_spectacular",
    "rest_framework",
    "rest_framework.authtoken",
    "user",
    "products",
    "articles",
    "pictures",
    "orders",
    "cities",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "api.core.pagination.ExtendedPageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

PASSWORDLESS_AUTH = {
    "PASSWORDLESS_AUTH_TYPES": ["EMAIL"],
    "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": os.getenv(
        "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS"
    ),
    "PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME": "email_callback_token_template.html",
    "PASSWORDLESS_AUTH_TOKEN_SERIALIZER": "user.serializers.TokenResponseSerializer",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Shoppe API",
    "DESCRIPTION": "This is full descriptive documentation of Shoppe API "
    "written on Django and Django Rest Framework",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "DISABLE_ERRORS_AND_WARNINGS": True,
}


SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DEFAULT_FILE_STORAGE = (
    "django.core.files.storage.InMemoryStorage"
    if os.getenv("TESTING", False)
    else "storages.backends.gcloud.GoogleCloudStorage"
)

GS_BUCKET_NAME = os.environ.get("GS_BUCKET_NAME")


WSGI_APPLICATION = "api.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DEFAULT_DB_NAME"),
        "USER": os.getenv("DEFAULT_DB_USER"),
        "PASSWORD": os.getenv("DEFAULT_DB_PASSWORD"),
    },
    "geocity": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("GEOCITY_DB_NAME"),
        "USER": os.getenv("GEOCITY_DB_USER"),
        "PASSWORD": os.getenv("GEOCITY_DB_PASSWORD"),
    },
}
DATABASE_ROUTERS = ["api.core.routers.GeoCityRouter"]

CITIES_FILES = {
    "city": {
        "filenames": ["UA.zip"],
    },
    "alt_name": {
        "filename": "alternateNamesV2.zip",
    },
}

CITIES_LOCALES = ["uk", "ru", "en", "und"]
CITIES_POSTAL_CODES = ["UA"]
CITIES_SKIP_CITIES_WITH_EMPTY_REGIONS = True


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"

MEDIA_URL = "/images/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

ALLOWED_FILE_EXTENSIONS = ["jpg", "jpeg", "png"]

AUTH_USER_MODEL = "user.User"
