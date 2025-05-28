from models import User, Source, Article, SavedArticle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup DB connection
engine = create_engine("sqlite:///newsradar.db")
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    while True:
        print("\n=== NewsRadar CLI ===")
        print("1. Manage Users")
        print("2. Manage Sources")
        print("3. Manage Articles")
        print("4. Manage Saved Articles")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            source_menu()
        elif choice == "3":
            article_menu()
        elif choice == "4":
            saved_article_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def user_menu():
    while True:
        print("\n-- User Menu --")
        print("1. Create User")
        print("2. View All Users")
        print("3. Find User by ID")
        print("4. Delete User")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            user = User.create(session, username=username, email=email, password=password)
            print(f"Created user: {user.username}")
        elif choice == "2":
            users = User.get_all(session)
            for u in users:
                print(f"{u.id}: {u.username} ({u.email})")
        elif choice == "3":
            id = int(input("Enter User ID: "))
            user = User.find_by_id(session, id)
            if user:
                print(f"{user.id}: {user.username} - {user.email}")
            else:
                print("User not found.")
        elif choice == "4":
            id = int(input("Enter User ID to delete: "))
            if User.delete(session, id):
                print("User deleted.")
            else:
                print("User not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def source_menu():
    while True:
        print("\n-- Source Menu --")
        print("1. Create Source")
        print("2. View All Sources")
        print("3. Find Source by ID")
        print("4. Delete Source")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Source name: ")
            source = Source.create(session, name=name)
            print(f"Created source: {source.name}")
        elif choice == "2":
            for s in Source.get_all(session):
                print(f"{s.id}: {s.name}")
        elif choice == "3":
            id = int(input("Enter Source ID: "))
            s = Source.find_by_id(session, id)
            if s:
                print(f"{s.id}: {s.name}")
            else:
                print("Source not found.")
        elif choice == "4":
            id = int(input("Enter Source ID to delete: "))
            if Source.delete(session, id):
                print("Source deleted.")
            else:
                print("Source not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def article_menu():
    while True:
        print("\n-- Article Menu --")
        print("1. Create Article")
        print("2. View All Articles")
        print("3. Find Article by ID")
        print("4. Delete Article")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            category = input("Category: ")
            source_id = int(input("Source ID: "))
            article = Article.create(session, title=title, content=content, category=category, source_id=source_id)
            print(f"Created article: {article.title}")
        elif choice == "2":
            for a in Article.get_all(session):
                print(f"{a.id}: {a.title} (Source: {a.source_id})")
        elif choice == "3":
            id = int(input("Enter Article ID: "))
            a = Article.find_by_id(session, id)
            if a:
                print(f"{a.id}: {a.title}, Category: {a.category}, Source: {a.source_id}")
            else:
                print("Article not found.")
        elif choice == "4":
            id = int(input("Enter Article ID to delete: "))
            if Article.delete(session, id):
                print("Article deleted.")
            else:
                print("Article not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def saved_article_menu():
    while True:
        print("\n-- Saved Articles Menu --")
        print("1. Save Article for User")
        print("2. View All Saved Articles")
        print("3. Find Saved Article by ID")
        print("4. Delete Saved Article")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            user_id = int(input("User ID: "))
            article_id = int(input("Article ID: "))
            saved = SavedArticle.create(session, user_id=user_id, article_id=article_id)
            print(f"Saved article {saved.article_id} for user {saved.user_id}")
        elif choice == "2":
            for s in SavedArticle.get_all(session):
                print(f"{s.id}: User {s.user_id} saved Article {s.article_id}")
        elif choice == "3":
            id = int(input("Enter Saved Article ID: "))
            s = SavedArticle.find_by_id(session, id)
            if s:
                print(f"{s.id}: User {s.user_id}, Article {s.article_id}, Saved at {s.saved_at}")
            else:
                print("Saved Article not found.")
        elif choice == "4":
            id = int(input("Enter Saved Article ID to delete: "))
            if SavedArticle.delete(session, id):
                print("Saved article deleted.")
            else:
                print("Saved article not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
