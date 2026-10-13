from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:1603@localhost:5432/backend_project"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)