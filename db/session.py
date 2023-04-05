from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# DB_URL = os.environ.get("DB_URL")

# if not DB_URL:
#     raise Exception("must supply database url")
DB_URL = "postgresql://postgres:password@localhost/realworldfast"

engine = create_engine(
    DB_URL
)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# database session generator


def get_db():
    # creata db session
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
