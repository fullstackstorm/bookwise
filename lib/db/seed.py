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

def create_books(authors):
    book_titles = [
        f"{fake.catch_phrase()} Mysteries: {fake.city()}",
        f"The Chronicles of {fake.first_name()} {fake.last_name()}",
        f"{fake.word.verb()} in the {fake.word.adjective()}",
        f"{fake.word.adjective()} {fake.word.noun()}",
        f"{fake.word.verb()} of {fake.word.noun()}",
        f"Adventures in the {fake.word.noun()}",
        f"Journey through {fake.word.noun()}",
        f"Reflections in {fake.word()}"
    ]
    
    books = []
    for author in authors:
        num_books = fake.random_int(min_books_per_author, max_books_per_author)
        for _ in range(num_books):
            title = fake.random_element(book_titles)
            book = Book(name=title)
            session.add(book)
            books.append(book)
    session.commit()
    return books

def create_users():
    users = []
    for _ in range(num_users):
        user = User(name=fake.user_name)
        users.append(user)
        session.add(user)
    session.commit()
    return users

def relate_one_to_many(authors, books, genres):
    pass

if __name__ == '__main__':
    delete_records()

    authors = create_authors()
    available_genres = create_genres()
    books = create_books()
    users = create_users()

    authors, books, available_genres = relate_one_to_many(authors, books, available_genres)
