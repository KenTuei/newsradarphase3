from sqlalchemy import (
    Column, Integer, String, Text, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    saved_articles = relationship("SavedArticle", back_populates="user")

    @classmethod
    def create(cls, session, **kwargs):
        user = cls(**kwargs)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def delete(cls, session, id):
        obj = session.query(cls).get(id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False


class Source(Base):
    __tablename__ = "sources"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    articles = relationship("Article", back_populates="source")

    @classmethod
    def create(cls, session, **kwargs):
        source = cls(**kwargs)
        session.add(source)
        session.commit()
        return source

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def delete(cls, session, id):
        obj = session.query(cls).get(id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False


class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    category = Column(String, nullable=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    source = relationship("Source", back_populates="articles")
    saved_by = relationship("SavedArticle", back_populates="article")

    @classmethod
    def create(cls, session, **kwargs):
        article = cls(**kwargs)
        session.add(article)
        session.commit()
        return article

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def delete(cls, session, id):
        obj = session.query(cls).get(id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False


class SavedArticle(Base):
    __tablename__ = "saved_articles"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    saved_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    user = relationship("User", back_populates="saved_articles")
    article = relationship("Article", back_populates="saved_by")

    @classmethod
    def create(cls, session, **kwargs):
        saved = cls(**kwargs)
        session.add(saved)
        session.commit()
        return saved

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def delete(cls, session, id):
        obj = session.query(cls).get(id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False



