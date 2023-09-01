#!/usr/bin/env python
from db.models import User
from simple_term_menu import TerminalMenu
from helpers import show_book_recommendations
import os

class Cli():
    def __init__(self):
        self.current_user = None

    def start(self):
        self.clear_screen()
        print("Welcome to BookWise! A CLI to give you new book recommendations.\n")
        options = ["Login", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "Login":
            self.handle_login()
            show_book_recommendations(self.current_user)
        else:
            self.exit()
  

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def handle_login(self):
        username = input("Enter your username, an account will be created if it doesn't exist:\n")
        user = User.login_or_create(username)
        self.current_user = user
        print(f"Hello, {user.name}!\n")


if __name__ == '__main__':
    cli = Cli()
    cli.start()
