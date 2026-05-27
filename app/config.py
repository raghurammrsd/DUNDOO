import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")

    DB_NAME = os.getenv("DB_NAME", "shopkeeper_db")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "mrsdmsrr")  
    
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_USER = os.getenv("EMAIL_USER", "msriraghuram@gmail.com")
    EMAIL_PASS = os.getenv("EMAIL_PASS", "usxqkvmvceifmdwm")  

    
    UPLOAD_FOLDER = os.path.join(basedir, "..", "static", "uploads", "products")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  

    
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")






    UPLOAD_REELS_FOLDER = os.path.join(basedir, "..", "static", "uploads", "reels")

    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MB (≈ 5 min 720p)

    ALLOWED_VIDEO_EXTENSIONS = {"mp4", "mov", "webm"}
