# BookWise CLI
BookWise is a simple app that allows you to login and select book genre preferences. From there, a list of book recommendations are given. Anytime you login, your list will be given to you.

## Installation
To run BookWise, follow these steps:
1. Fork and clone:
    ```shell
    git clone git@github.com:<username>/bookwise.git
    ```
2. Navigate to the repository and install the dependencies:
    ```shell
    pipenv install
    ```
3. Open your virtual environment:
    ```shell
    pipenv shell
    ```
4. Navigate to the alembic.ini directory and create the database:
    ```shell
    cd lib/db
    alembic upgrade head
    ```
5. Navigate back to the lib folder, seed the database, and run BookWise:
    ```shell
    cd ..
    python seed.py
    python cli.py
    ```

The CLI should now be running!

## Usage
1. Use your arrow keys to select wether you want to login or exit the application. Press enter to continue.

2. If you login, type your username. An account will be created if you don't already have one. If you already have an account, step 3 will be skipped.

3. A selection menu of genres will be displayed. Move your arrow keys to a preferred genre and hit enter. You can select as many genres as you want. The menu will dissappear after you select 'Done'.

4. Once you select 'Done' or once you login to an existing account, a list of book recommendations will appear!

## Contributing

You are welcome to fork this repository and make changes, but I will not be accepting these changes.
This project is designed for me to sharpen my web development skills overtime.

## Licensing

Both [Faker](https://pypi.org/project/Faker/) and [WonderWords](https://pypi.org/project/wonderwords/) were used in the making of this project.