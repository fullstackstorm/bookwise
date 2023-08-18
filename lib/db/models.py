from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

author_genre_association = Table(
    'author_genre_association',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

preferred_author_association = Table(
    'preferred_authors',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

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
    genres = relationship(
        'Genre', 
        secondary=author_genre_association, 
        back_populates='authors'
    )
    preferred_by_users = relationship(
        'User', 
        secondary=preferred_author_association, 
        back_populates='preferred_authors'
    )

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    author_id = Column(Integer(), ForeignKey('authors.id'), nullable=False)
    genre_id = Column(Integer(), ForeignKey('genres.id'), nullable=False)

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    authors = relationship(
        'Author', 
        secondary=author_genre_association,
        back_populates='genres'
    )
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

    preferred_authors = relationship(
        'Author', 
        secondary=preferred_author_association, 
        back_populates='preferred_by_users'
    )
    preferred_genres = relationship(
        'Genre',
        secondary=preferred_genre_association,
        back_populates='preferred_by_users'
    )