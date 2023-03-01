from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': '',
    'database': 'test'
}
#SQLALCHEMY_DATABASE_URL = URL(**DATABASE)
#connection = psycopg2.connect(user="postgres", password="")

#SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres@localhost:5432/test"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/test"

engine = create_engine(
    #SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

