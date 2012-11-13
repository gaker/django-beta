# test_settings
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "jkhasdfjhdfsFS%^*asdfjkh!!"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'beta',
    'django_nose',
]

SITE_ID = 1

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'tests/templates'),
    os.path.join(BASE_DIR, 'templates'),
)

ROOT_URLCONF = 'beta.tests.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
