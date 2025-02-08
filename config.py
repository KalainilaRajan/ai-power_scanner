import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Use SQLite for the database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///resumes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for better performance
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecretkey')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

class DevelopmentConfig(Config):
    # Configuration for development mode
    DEBUG = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'