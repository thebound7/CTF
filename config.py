import os

SECRET_KEY = 'p4ssw0rd_c0d3'
SECURITY_PASSWORD_SALT = 'my_s3cUr3_s4lt'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')

# Recaptcha
RECAPTCHA_PRIVATE_KEY = '6LcYHxETAAAAAOygGs3kv5AsLtQaRpk0P5bq-rCD'
RECAPTCHA_PUBLIC_KEY = '6LcYHxETAAAAAC1rLdVTL2wzokzbn01eVjVbYsl3'
RECAPTCHA_PARAMETERS = {'hl': 'zh', 'render': 'explicit'}
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}

# mail settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# gmail authentication
MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']


# mail accounts
MAIL_DEFAULT_SENDER = 'amriabdesslem@gmail.com'

