class Config():
    DEBUG = False 
    SQLALCHEMY_TRACK_MODIFICATIONS = True 
    
    
class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin123@localhost/placement_portal" 
    SECRET_KEY = "secret-key-here"