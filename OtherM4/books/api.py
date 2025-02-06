from flask import Flask, request, jsonify

# import necessary modules from flask and sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# setting Flask App
app = Flask(__name__)

# configure database for flask using sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Sample list of books (initial data, if needed)
books = [
    {'title': 'The Weirdstone of Brisingamen', 'author': 'Alan Garner', 'year': 1960},
    {'title': 'Perdido Street Station', 'author': 'China Miéville', 'year': 2000},
    {'title': 'Thud!', 'author': 'Terry Pratchett', 'year': 2005},
    {'title': 'The Spellman Files', 'author': 'Lisa Lutz', 'year': 2007},
    {'title': 'Small Gods', 'author': 'Terry Pratchett', 'year': 1992}
]

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(80), unique=True, nullable=False)
    book_author = db.Column(db.String(50))
    book_publisher = db.Column(db.String(80))

    def __repr__(self):  # representation with self for objects
        return f"{self.id} - {self.book_title} - {self.book_author} - {self.book_publisher}"

@app.route('/books', methods=['GET'])
def get_books() -> dict:
    """
    Get all books in database

    Returns:
        dict: dictionary of all books in the database
    """
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_title': book.book_title,
            'book_author': book.book_author,
            'book_publisher': book.book_publisher
        }
        output.append(book_data)
    return {'books': output}

@app.route('/books', methods=['POST'])
def create_book() -> dict:
    """
    Create a new book for the database

    Returns:
        dict: message and ID of the added book
    """
    book = Book()
    book.id = request.json['id']
    book.book_title = request.json['book_title']
    book.book_author = request.json['book_author']
    book.book_publisher = request.json['book_publisher']
    
    db.session.add(book)
    db.session.commit()
    
    return {'message': 'Added Successfully', 'id': book.id}

# create link for local book from DB
# http://localhost:5000/books/1 
@app.route('/books/<id>', methods=['PUT'])
def update_book(id: int) -> dict:
    """
    Update book details with ID

    Returns:
        dict: confirmation message with updated fields
    """
    book = Book.query.get_or_404(id)
    
    book.book_title = request.json['book_title']
    book.book_author = request.json['book_author']
    book.book_publisher = request.json['book_publisher']
    
    db.session.commit()
    
    return {
        "message": "Book updated successfully",
        "updated_fields": {
            "book_title": book.book_title,
            "book_author": book.book_author,
            "book_publisher": book.book_publisher
        }
    }

# create link for local book from DB
# http://localhost:5000/books/1   
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id: int) -> dict:
    """
    Delete a book from the database

    Returns: confirmation message with book ID or error if not found
    """
    book = Book.query.get(id)
    if book is None:
        return {'error': f'Book {id} not found'}
    
    db.session.delete(book)
    db.session.commit()
    
    return {'message': f'Book {id} deleted successfully'}

if __name__ == "__main__":
    app.run(debug=True)
