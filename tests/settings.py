import time
import os

DEBUG = True
USE_TZ = True

INSTALLED_APPS = [
    "django_spanner",  # Must be the first entry
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tests",
]

TIME_ZONE = "UTC"

ENGINE = "django_spanner"
PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT", os.getenv("PROJECT_ID", "emulator-test-project"),
)

INSTANCE = "django-test-instance"
NAME = "spanner-django-test-{}".format(str(int(time.time())))

DATABASES = {
    "default": {
        "ENGINE": ENGINE,
        "PROJECT": PROJECT,
        "INSTANCE": INSTANCE,
        "NAME": NAME,
    }
}
SECRET_KEY = "spanner emulator secret key"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
