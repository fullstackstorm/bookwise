#!/usr/bin/env python
from db.models.user import BookWiseUser

class Cli():
    def __init__(self):
        current_user = None

    def start(self):
        menu = True
        print("Welcome to BookWise! A CLI to give you new book recommendations.\n")
        while menu:
            print("1. Login")
            print("2. Exit\n")
            user_input = input("Enter a selection (1-2):\n")
            if user_input in ['1', '2']:
                self.handle_user_input(user_input)
                menu = False
            else:
                print("Invalid selection. Please choose 1 or 2.")

    def second_menu():
        pass

    def handle_user_input(choice):
        if choice == '1':
            current_user = BookWiseUser.login_or_create()
        elif choice == '2':
            print("Exiting the program.")


    if __name__ == '__main__':
        start()
