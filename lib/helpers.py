from db.models import Genre, Book
from db.session import Session

session = Session()

def get_recommendation_table(genre_name, session = session):
    recommended_books = (
        session.query(Book, Genre.name.label('genre_name'))
        .join(Genre, Genre.id == Book.genre_id)
        .filter(Genre.name == genre_name)
        .all()
    )
    return recommended_books

def print_recommendation_table(recommended_books):
    for book, genre_name in recommended_books:
        print("Book:", book.name)
        print("Author:", book.author.name)
        print("Genre:", genre_name)
        print("===")

def show_book_recommendations(current_user):
    recommended_books = []

    # Iterate through the user's preferred genres and retrieve recommendations
    for genre in current_user.preferred_genres:
        recommended_books.extend(get_recommendation_table(genre.name))

    print_recommendation_table(recommended_books)
