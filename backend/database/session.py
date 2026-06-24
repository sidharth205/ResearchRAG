from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency — gives each request its own DB session,
    and guarantees it's closed afterward even if an error occurs.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()