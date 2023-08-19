from .models import User
from db.session import Session

session = Session()

class BookWiseUser(User):

    def __init__(self):
        self.user = None

    @classmethod
    def login_or_create(cls):
        username = input("Enter your username, an account will be created if it doesn't exist:\n")
        user = session.query(cls).filter_by(name=username).first()
        if user:
            return user
        else:
            cls.user = BookWiseUser(name=username)
            session.add(cls.user)
            session.commit()
            return cls.user