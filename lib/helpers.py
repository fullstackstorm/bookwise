from db.models import Genre, Book
from db.session import Session

session = Session()

def get_recommendation_table(genre_name, session = session):
    genre = session.query(Genre).filter_by(name=genre_name).first()

    recommended_books = (
        session.query(Book)
        .join(Genre, Genre.id == Book.genre_id)
        .filter(Genre.id == genre.id)
        .all()
    )
    return recommended_books

def print_recommendation_table(recommended_books):
    for book in recommended_books:
        print("Book:", book.name)
        print("Author:", book.author.name)
        print("===")

def show_book_recommendations(current_user):
    recommended_books = []

    # Iterate through the user's preferred genres and retrieve recommendations
    for genre in current_user.preferred_genres:
        recommended_books.extend(get_recommendation_table(genre.name))

    print_recommendation_table(recommended_books)
