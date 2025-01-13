from flask_sqlalchemy import SQLAlchemy

# Initialize the db
db = SQLAlchemy()

# Define the Author model
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    # Create string representation
    def __repr__(self):
        return f"<Author {self.name} (ID: {self.id})>"

# Define the Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    cover_url = db.Column(db.String(500), nullable=True)
    publication_year = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', cascade='all, delete'))

    def __repr__(self):
        return f"<Book {self.title} by {self.author.name if self.author else 'Unknown Author'}>"