#!/usr/bin/env python
from db.models.user import BookWiseUser

current_user = BookWiseUser()

def start():
    print("Welcome to BookWise! A CLI to give you new book recommendations.\n")
    while True:
        print("1. Login")
        print("2. Exit\n")
        user_input = input("Enter a selection (1-2):\n")
        if user_input in ['1', '2']:
            handle_user_input(user_input)
            if user_input == '2':
                break
        else:
            print("Invalid selection. Please choose 1 or 2.")

def handle_user_input(choice):
    if choice == '1':
        current_user.login_or_create()
    elif choice == '2':
        print("Exiting the program.")


if __name__ == '__main__':
    start()
