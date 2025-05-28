# NewsRadar CLI

**NewsRadar CLI** is a Python-based command-line interface application that allows users to manage news-related data including users, sources, articles, and saved articles using SQLAlchemy ORM and a SQLite database.

## Features

- Manage Users: Create, view, find, and delete users
- Manage Sources: Add and manage news sources
- Manage Articles: Create and organize articles by category and source
- Saved Articles: Let users save articles for later

## Tech Stack

- Python 3.10+
- SQLAlchemy ORM
- SQLite (default database)
- Faker (for generating seed data)

## Install Dependencies
- It’s recommended to use a virtual environment.
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate
- pip install -r requirements.txt
- If you don’t have a requirements.txt, install manually:
   pip install sqlalchemy faker

## Seed the Database
Run the following to create tables and populate the database with sample data:
python seed.py
This will generate:
10 users
5 sources
20 articles
30 saved articles

## Run the Application
---python lib/db/cli.py
Navigate the interactive menus to manage users, sources, articles, and saved articles.
  ## CLI Menus
Main Menu
=== NewsRadar CLI ===
1. Manage Users
2. Manage Sources
3. Manage Articles
4. Manage Saved Articles
5. Exit
Example Actions
Create and view users

Link users to saved articles

View all sources and articles

Delete users, articles, and sources by ID

 ## Configuration
Default database: newsradar.db (SQLite)
engine = create_engine("sqlite:///newsradar.db")
 ## Security Note
Passwords are stored as plain text in this demo project. In real applications, always hash passwords using libraries like bcrypt.



