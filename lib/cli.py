#!/usr/bin/env python

#!/usr/bin/env python

def start():
    print("Welcome to BookWise! A CLI to give you new book recommendations.\n")
    while True:
        print("1. Create a New Account")
        print("2. Login to an Existing Account")
        print("3. Exit")
        user_input = input("Enter a selection (1-3): ")
        if user_input in ['1', '2', '3']:
            handle_user_input(user_input)
            if user_input == '3':
                break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

def handle_user_input(choice):
    if choice == '1':
        create_account()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the program.")

def create_account():
    # Implementation for creating a new account
    print("Creating a new account.")

def login():
    # Implementation for logging in
    print("Logging in.")

if __name__ == '__main__':
    start()
