#import ipdb; ipdb.set_trace()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from wonderwords import RandomWord
from models import Author, Book, Genre, User

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()
word = RandomWord()

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
        author = Author(name=f"{fake.first_name()} {fake.last_name()}")
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
    adjectives = word.filter(include_parts_of_speech=["adjectives"])
    verbs = word.filter(include_parts_of_speech=["verbs"])
    nouns = word.filter(include_parts_of_speech=["nouns"])

    book_titles = [
        f"{fake.catch_phrase()} Mysteries: {fake.city()}",
        f"The Chronicles of {fake.first_name()} {fake.last_name()}",
        f"{fake.random_element(verbs)} in the {fake.random_element(adjectives)}",
        f"{fake.random_element(adjectives)} {fake.random_element(nouns)}",
        f"{fake.random_element(verbs)} of {fake.random_element(nouns)}",
        f"Adventures in the {fake.random_element(nouns)}",
        f"Journey through {fake.random_element(nouns)}",
        f"Reflections in {fake.word()}"
    ]
    
    books = []
    for _ in range(len(authors)):
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
        user = User(name=fake.user_name())
        users.append(user)
        session.add(user)
    session.commit()
    return users

def establish_relationships(authors, books, genres, users):
    for book in books:
        author = fake.random_element(authors)
        genre = fake.random_element(genres)

        book.author_id = author.id
        book.genre_id = genre.id

        author.books.append(book)
        genre.books.append(book)

    for user in users:
        user_preferred_genres = fake.random_elements(elements=genres, length=3, unique=True)
        user.preferred_genres.extend(user_preferred_genres)

if __name__ == '__main__':
    try:
        delete_records()

        authors = create_authors()
        genres = create_genres()
        books = create_books(authors)
        users = create_users()

        establish_relationships(authors, books, genres, users)

        session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()  # Rollback the session in case of an exception
    finally:
        session.close()  # Always close the session
