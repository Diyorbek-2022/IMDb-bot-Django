import os
from pathlib import Path

from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # --- 3rd-party ---
    "jazzmin",  # admin UI (birinchi)
    "corsheaders",
    "rest_framework",

    # --- Django ---
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # --- Project apps ---
    "Users",
    "Cinema",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # whitenoise #
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # corsheaders #
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'Bot_Main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Bot_Main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / "static"]  # agar qo‘shimcha static papkang bo‘lsa

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# settings.py

# settings.py

JAZZMIN_SETTINGS = {
    # --- Brand ---
    "site_title": "MyDB Cinema — Admin",
    "site_header": "MyDB Cinema",
    "site_brand": "MyDB Cinema",
    "welcome_sign": "Xush kelibsiz!",
    "copyright": "© 2025 MyDB Cinema",

    # Logo & Icon
    "site_logo": "img/logo.png",
    "site_logo_classes": "img-circle elevation-3",
    "site_icon": "img/favicon.png",
    "login_logo": "img/logo.png",
    "login_logo_dark": None,

    # --- UI & Navigation ---
    "show_ui_builder": False,
    "navigation_expanded": True,
    "hide_version": True,         # <<< Jazzmin Version 3.0.1 yo‘qoladi

    # --- Top menu links ---
    "topmenu_links": [
        {"name": "Foydalanuvchilar", "url": "admin:Users_user_changelist", "permissions": ["Users.view_user"]},
        {"name": "Kinolar", "url": "admin:Cinema_cinema_changelist"},
        {"name": "DRF API", "url": "/api/v1/"},
        {"name": "Admin bosh sahifa", "url": "admin:index"},
    ],

    # --- Ikonkalar ---
    "icons": {
        "admin.LogEntry": "fas fa-file-alt",
        "auth": "fas fa-users-cog",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",

        "Users": "fas fa-user-friends",
        "Users.User": "fas fa-user",
        "Users.Info": "fas fa-id-badge",
        "Users.Favorite": "fas fa-heart",
        "Users.Showed": "fas fa-eye",

        "Cinema": "fas fa-film",
        "Cinema.Cinema": "fas fa-video",
    },

    # --- Sidebar tartibi ---
    "order_with_respect_to": [
        "Users",
        "Users.User",
        "Users.Info",
        "Users.Favorite",
        "Users.Showed",
        "Cinema",
        "Cinema.Cinema",
        "auth",
        "admin.LogEntry",
    ],

    # --- Custom linklar ---
    "custom_links": {
        "Users": [
            {"name": "Aktiv foydalanuvchilar", "url": "admin:Users_user_changelist", "icon": "fas fa-user-check", "permissions": ["Users.view_user"]},
        ],
        "Cinema": [
            {"name": "Yangi kino qo‘shish", "url": "admin:Cinema_cinema_add", "icon": "fas fa-plus-circle"},
        ],
    },

    # --- User menu ---
    "user_menu_links": [
        {"model": "auth.user"},
        {"name": "Parolni o‘zgartirish", "url": "admin:password_change"},
        {"name": "Chiqish", "url": "admin:logout"},
    ],

    # --- Changeform ---
    "related_modal_active": True,
    "show_breadcrumbs": True,
    "hide_save_buttons": False,   # <<< Saqlash tugmalari ko‘rinadi

    # --- Qidiruv ---
    "search_model": ["Users.User", "Cinema.Cinema"],

    # --- Til ---
    "language_chooser": False,
    "custom_css": "css/admin.css",
}


JAZZMIN_UI_TWEAKS = {
    # --- Theme ---
    "theme": "flatly",           # bootstrap5 temasi (chiroyli ko‘k)
    "dark_mode_theme": "darkly", # tunda qora tema

    # --- Navbar & Sidebar ---
    "navbar": "navbar-dark navbar-primary",   # yuqori menyu
    "navbar_fixed": True,
    "sidebar": "sidebar-dark-success",        # chap menyu
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "brand_small_text": False,

    # --- Body & Footer ---
    "body_small_text": False,
    "footer_fixed": True,

    # --- Forms & Inputs ---
    "accent": "accent-success",               # input chizig‘i yashil
    "button_classes": {
        "primary": "btn btn-success",  # Asosiy knopka (saqlash) yashil bo‘ladi
        "secondary": "btn btn-secondary",
        "info": "btn btn-info",
        "warning": "btn btn-warning",
        "danger": "btn btn-danger",
        "success": "btn btn-success",
    },
    "primary_color": "green",

    # --- Rounding & Shadow ---
    "round_borders": True,
    "card_rounded": True,
    "cards": "card-outline card-success shadow-lg",
    "login_logo": None,

    # --- Dark mode tugmasi ---
    "show_dark_mode_toggle": True,
}
