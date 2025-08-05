# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Dirección de la base de datos SQLite
DATABASE_URL = "sqlite:///./metro.db"  # Puedes cambiar "metro.db" por otro nombre

# Motor de conexión a SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para modelos ORM
Base = declarative_base()
