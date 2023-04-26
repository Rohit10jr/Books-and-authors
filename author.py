from flask_sqlalchemy import SQLAlchemy
from .app import app, db
from .book import Book


class Author(db.Model):
     __tablename__ = "authors"
     auhtor_id = db.Column(db.Integer, primary_key=True)
     author_names = db.Column(db.String(225))
     book_names = db.Column(db.String(255))
     #price = db.column(db.integer, primary_key=True) 
     books = db.relationship(Book, backref='author')
    
     def __init__(self, author_id, author_name, book_name):
           self.author_id = author_id
           self.author_name = author_name
           self.book_name = book_name
           #self.price = price

  
     def __repr__(self):
        return '%s/%s/%s' % (self.auhtor_id, self.author_name, self.book_name)

            