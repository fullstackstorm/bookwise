import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = os.path.join(os.path.dirname(__file__), 'library.db')
engine = create_engine(f'sqlite:///{database_url}')
Session = sessionmaker(bind=engine)