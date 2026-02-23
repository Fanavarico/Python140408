#DATABASE SAKHTE BESHE (koli table tooshe)
#table? --> models.py
#hatman pip install SQLalchemy bashe
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base ,sessionmaker

#motor misaze
engine = create_engine('sqlite:///database.db', echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    return SessionLocal()


