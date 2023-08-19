#!/usr/bin/env python

def start():
    print("Welcome to BookWise! A CLI to give you new book recommendations.\n")
    print("1. Create a New Account")
    print("2. Login to an Existing Account")
    print("3. Exit")
    user_input = input("Enter a selection (1-3)")
    handle_user_input(user_input)

if __name__ == '__main__':
    pass