# filepath: c:\Users\Relanto\Documents\AutoResume\src\db\init_db.py
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URL
from .models import Base

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)
print("Database tables created (or already exist).")