from flask_sqlalchemy import SQLAlchemy


# Initialize the db.
db = SQLAlchemy()


# Define the Author model
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    date_of_death = db.Column(db.Date, nullable=False)

    # Custom string representation
    def __repr__(self):
        return f"<Author {self.name} (ID: {self.id})"
    
    def __str__(self):
        return f"{self.name}, born {self.birth_date}"
    

# Define the Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer, nullable=True)

    # Foreign key to the Author table
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    # Relationship to access the author from a book instance
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    # Custom string representation
    def __repr__(self):
        return f"<Book {self.title} (ID: {self.id}, Author: {self.author_name})>"
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
