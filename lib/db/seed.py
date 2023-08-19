from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, Author, Book, Genre, User
import ipdb; ipdb.set_trace()

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

available_genres = ['Mystery', 'Science Fiction', 'Fantasy', 'Romance', 'Thriller', 'Historical', 'Adventure']

num_authors = 30
min_books_per_author = 3
max_books_per_author = 10
num_users = 5

def delete_records():
    session.query(Author).delete()
    session.query(Book).delete()
    session.query(Genre).delete()
    session.query(User).delete()
    session.commit()

def create_authors():
    authors = []
    for _ in range(num_authors):
        author = Author(name=fake.full_name())
        authors.append(author)
        session.add(author)
    session.commit()
    return authors

def create_genres():
    genres = []
    for name in available_genres:
        genre = Genre(name=name)
        genres.append(genre)
        session.add(genre)
    session.commit()
    return genres

def create_books():
    pass

def create_users():
    pass

def relate_one_to_many(authors, books, genres):
    pass

if __name__ == '__main__':
    delete_records()

    authors = create_authors()
    available_genres = create_genres()
    books = create_books()
    users = create_users()

    authors, books, available_genres = relate_one_to_many(authors, books, available_genres)
