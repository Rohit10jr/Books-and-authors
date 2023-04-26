from flask_sqlalchemy import SQLAlchemy
from .app import app, db

class Book(db.Model):
     __tablename__ = "users"
     bookid = db.Column(db.Integer, primary_key=True)
     bookname = db.Column(db.String(225))
     authorname = db.Column(db.String(255))
     #price = db.column(db.integer, primary_key=True) 
     authors = db.Column(db.Integer, db.ForeignKey('Author.author_id'))

     def __init__(self, bookid, bookname, authorname):
           self.bookid = bookid
           self.bookname = bookname
           self.authorname = authorname
           #self.price = price

  
     def __repr__(self):
        return '%s/%s/%s' % (self.bookid, self.bookname, self.authorname)
