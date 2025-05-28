from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime
import random

from models import User, Source, Article, SavedArticle

engine = create_engine("sqlite:///newsradar.db")
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
fake = Faker()

# Seed users
users = []
for _ in range(10):
    user = User(
        username=fake.unique.user_name(),
        email=fake.unique.email(),
        password=fake.password()
    )
    session.add(user)
    users.append(user)

# Seed sources
sources = []
for _ in range(5):
    source = Source(
        name=fake.unique.company()
    )
    session.add(source)
    sources.append(source)

# Seed articles
articles = []
categories = ["Politics", "Technology", "Health", "Business", "Sports"]
for _ in range(20):
    article = Article(
        title=fake.sentence(nb_words=6),
        content=fake.text(max_nb_chars=2000),
        category=random.choice(categories),
        source=random.choice(sources),
        published_at=fake.date_time_this_year()
    )
    session.add(article)
    articles.append(article)

# Seed saved_articles
for _ in range(30):
    saved_article = SavedArticle(
        user=random.choice(users),
        article=random.choice(articles),
        saved_at=fake.date_time_this_year()
    )
    session.add(saved_article)

session.commit()
print("Database seeded successfully.")
