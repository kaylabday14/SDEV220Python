from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up the Flask application and database connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(80), unique=True, nullable=False)
    book_author = db.Column(db.String(50))
    book_publisher = db.Column(db.String(80))

def display_books_alphabetical():
    # Get all books from the database ordered by book_title
    books = Book.query.order_by(Book.book_title).all()
    
    # Print books in alphabetical order
    for book in books:
        print(f"Title: {book.book_title}, Author: {book.book_author}, Publisher: {book.book_publisher}")

if __name__ == "__main__":
    with app.app_context():
        display_books_alphabetical()
