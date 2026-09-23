from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.config import settings

engine = create_engine(settings.DB_URL, pool_pre_ping=True, pool_size=10, max_overflow=20)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = DeclarativeBase()

def get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

