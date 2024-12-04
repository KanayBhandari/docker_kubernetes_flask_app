import os

USERNAME = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
HOSTNAME = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_DATABASE')
SECRET_KEY = os.environ.get('SECRET_KEY')
SCHEMA_NAME = os.environ.get('DB_SCHEMA_NAME')
PORT = os.environ.get('DB_PORT')

# Fetching values from env variables and replacing here to form the database_url
DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}?options=-c%20search_path%3D{SCHEMA_NAME}'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-any-random-characters'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False