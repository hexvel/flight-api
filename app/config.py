import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db_ip = os.getenv("DB_IP")
    db_name = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{db_ip}/{db_name}"

    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
