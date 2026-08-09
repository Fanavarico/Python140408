
#Pip install sqlalchemy --> create_engine --> db ag bod k bod, nabod misakht

from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base ,sessionmaker

#yek file besaz bename quiz.db tamame datahaye in appo in too hast
engine = create_engine('sqlite:///quiz.db', echo=False)

SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    return SessionLocal()


