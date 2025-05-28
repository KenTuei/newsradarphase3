# NewsRadar CLI

**NewsRadar CLI** is a clean and intuitive backend application that allows users to manage a news aggregation database directly from the command line. Built with Python and SQLAlchemy, it offers full CRUD functionality for managing users, news sources, articles, and saved (bookmarked) articles.

This tool is ideal for backend developers, testers, or anyone who wants to interact with and manipulate a news database without a graphical interface.

---

## Features

- **User Management:** Create, view, find, and delete user records.
- **Source Management:** Add and organize trusted news sources.
- **Article Management:** Create and filter news articles by category and source.
- **Bookmarking:** Let users save news articles to revisit later.
- **Interactive CLI:** Navigate a menu-based terminal interface with ease.
- **Seed Script:** Populate your database with fake data using `Faker`.

---

## User Stories

### 🔹 Manage Users  
> As a user, I can create and manage user profiles so that I can link them to saved articles.

### 🔹 Manage Articles and Sources  
> As a user, I can create, view, and organize news articles by categories and sources.

### 🔹 Bookmark Articles  
> As a user, I can save articles to my profile so I can read them later.

### 🔹 Work from the Terminal  
> As a user, I can interact with the database using a terminal-based menu so I don’t need a web frontend.

---

## How It Works

NewsRadar CLI uses SQLAlchemy to define models and interact with a SQLite database. It features:

- `models.py`: Defines the structure for Users, Sources, Articles, and SavedArticles.
- `cli.py`: The main entry point, offering a fully navigable CLI.
- `seed.py`: Generates test data using Faker (users, articles, sources, and bookmarks).
- `newsradar.db`: SQLite database created and managed through the application.

---

## Technologies Used

- **Python 3.10+**
- **SQLAlchemy** (ORM for DB interactions)
- **SQLite** (local development database)
- **Faker** (for fake seed data)
- **CLI Interface** using built-in `input()` and menu structures

---

## Getting Started

### Prerequisites

- Python 3.10 or newer installed
- A terminal or command prompt
- Git (optional for cloning the repo)

### Setup Instructions

#### 1. Clone the Repository

git clone https://github.com/KenTuei/newsradarphase3
cd newsradar-cli
 ## Install Dependencies
- It’s recommended to use a virtual environment.(pipenv install & pipenv shell)
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
- python lib/db/cli.py
- Navigate the interactive menus to manage users, sources, articles, and saved articles.
  ## CLI Menus
- Main Menu
- === NewsRadar CLI ===
1. Manage Users
2. Manage Sources
3. Manage Articles
4. Manage Saved Articles
5. Exit
- Actions

1. Create and view users
2. Link users to saved articles
3. View all sources and articles
4. Delete users, articles, and sources by ID

## Contribution
Contributions are welcome!
To contribute:
Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes
Push to your branch and open a Pull Request
 ## Security Note
Passwords are stored as plain text in this demo project. In real applications, always hash passwords using libraries like bcrypt.

## Author
[Ken Tuei](https://github.com/KenTuei)

## License
This project is licensed under the MIT License.

