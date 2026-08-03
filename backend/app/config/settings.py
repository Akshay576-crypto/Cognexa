import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # MySQL Configuration
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    # JWT Configuration
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
    )

    
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads",
    "documents"
            )
    QDRANT_HOST = "localhost"
    QDRANT_PORT = 6333

    
settings = Settings()
