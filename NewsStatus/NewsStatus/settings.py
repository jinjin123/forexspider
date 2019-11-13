# coding=utf-8
import os
import djcelery
import pymysql

DEBUG = False
SERVER_IP ='192.168.50.100'

"""
djcelery.setup_loader()
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_TASK_RESULT_EXPIRES = 1000
CELERYD_MAX_TASKS_PER_CHILD = 200
# CELERYD_FORCE_EXECV = True
CELERYD_TASK_TIME_LIMIT = 10 * 60 * 60
CELERY_IGNORE_RESULT = True
CELERY_TIMEZONE = 'Asia/Shanghai'
BROKER_URL = '%s' % SERVER_IP
BROKER_TRANSPORT = 'amqp'
"""
#BROKER_URL = '127.0.0.1'
#BROKER_TRANSPORT = 'redis'
#CELERY_RESULT_BACKEND = 'redis://%s:6379/0' % SERVER_IP
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'zej+b70@fwyqxz4cb!13-^t5kw*-#^y0n603oup^x=+r^-o0_z'

ADMINS=()
ALLOWED_HOSTS = ['*']

#CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'
CRONTAB_COMMAND_PREFIX = 'sleep 15;'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    #'djcelery',
    'django_crontab',
]

CRONJOBS = [
    ('* * * * *', 'news.cron.jten_news','>>/root/project/news/logs/cron.log'),
    ('*/30 * * * *', 'news.cron.static_news','>>/root/project/news/logs/cron.log'),
    ('*/1 * * * *', 'news.cron.trump_news','>>/root/project/news/logs/cron.log')
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewsStatus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'NewsStatus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "spiderflow",
	'USER': "root",
	'PASSWORD': 'zxc123',
	'HOST': SERVER_IP,
	'port': '3306',
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = (
#"%s/%s" % (BASE_DIR, "upload"),
#"%s/%s" % (BASE_DIR, "static"),
#)


SESSION_COOKIE_DOMAIN = None
CSRF_COOKIE_DOMAIN = None
SESSION_COOKIE_AGE = 3600 * 24

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(funcName)s %(lineno)d: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
	'django_crontab': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/') + 'crontab.log',
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {  # 发送邮件通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],  # 仅当 DEBUG = False 时才发送邮件
            'include_html': True,
        },
        'file_handler': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/') + 'main.log',
            'formatter': 'verbose'
        },
        'console': {  # 输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'cmdb_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/') + 'cmdb_info.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
	'django_crontab.crontab': {
            'handlers': ['django_crontab'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.request': {
            'handlers': ['file_handler', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'cmdb_log': {
            'handlers': ['cmdb_info'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

