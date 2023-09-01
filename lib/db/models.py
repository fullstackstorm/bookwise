from sqlalchemy import Column, Integer, String, ForeignKey, Table
from simple_term_menu import TerminalMenu
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .session import Session
import ipdb

session = Session()

Base = declarative_base()

preferred_genre_association = Table(
    'preferred_genres',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    books = relationship('Book', backref='author')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    author_id = Column(Integer(), ForeignKey('authors.id'))
    genre_id = Column(Integer(), ForeignKey('genres.id'))

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    books = relationship('Book', backref='genres')
    preferred_by_users = relationship(
        'User',
        secondary=preferred_genre_association,
        back_populates='preferred_genres'
    )

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    preferred_genres = relationship(
        'Genre',
        secondary=preferred_genre_association,
        back_populates='preferred_by_users'
    )

    @classmethod
    def login_or_create(cls, username):
        user = session.query(cls).filter_by(name=username).first()
        if user:
            return user
        else:
            new_user = User(name=username)
            session.add(new_user)
            new_user.capture_preferred_genres()
            
            session.commit()
            return new_user
    
    def capture_preferred_genres(self):
        genres = session.query(Genre).all()
        genre_names = [genre.name for genre in genres]
        genre_names.append('Done')
        preferred_genres = []
        print("\n")

        while True:
            menu = TerminalMenu(genre_names, title="Select Your Preferred Genre (Select 'Done' to finish):")
            selected_index = menu.show()
            
            if genre_names[selected_index] == 'Done':
                break
            
            preferred_genre_id = genres[selected_index].id
            # Query the Genre object by ID and store it
            preferred_genre = session.query(Genre).filter_by(id=preferred_genre_id).one()
            preferred_genres.append(preferred_genre)

        self.preferred_genres.extend(preferred_genres)
        session.commit()
