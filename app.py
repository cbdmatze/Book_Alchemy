from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from dotenv import load_dotenv
from data_models import db, Author, Book
from forms import AddAuthorForm, AddBookForm, RateBookForm
from utils import fetch_book_cover
import os
import openai

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
migrate = Migrate(app, db)

# Load environment variables form a .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)

# Route to add an author
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        new_author = Author(name=form.name.data, birth_date=form.birth_date.data)
        db.session.add(new_author)
        db.session.commit()
        flash('Author added successfully!', 'success')  # Flash message for success
        return redirect(url_for('add_author'))
    return render_template('add_author.html', form=form)

# Route to add a book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    if form.validate_on_submit():
        cover_url = fetch_book_cover(form.isbn.data)
        new_book = Book(
            title=form.title.data,
            isbn=form.isbn.data,
            cover_url=cover_url,
            author_id=form.author.data,
            publication_year=form.publication_year.data
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!', 'success')  # Added flash message for success
        return redirect(url_for('home'))  # Redirect to home to view all books
    return render_template('add_book.html', form=form)

# Route to display books on the home page
@app.route('/')
def home():
    sort_by = request.args.get('sort_by', 'title')
    if sort_by == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.order_by(Book.title).all()
    
    # Add a condition to handle when there are no books
    return render_template('home.html', books=books)

# Route to view book details
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    form = RateBookForm()
    return render_template('book_detail.html', book=book, form=form)

# Route to rate a book
@app.route('/book/<int:book_id>/rate', methods=['POST'])
def rate_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = RateBookForm()
    if form.validate_on_submit():
        book.rating = form.rating.data
        db.session.commit()
        flash('Rating submitted!', 'success')
    return redirect(url_for('book_detail', book_id=book_id))  # Redirect to book details

# Route to delete an author
@app.route('/author/<int:author_id>/delete', methods=['POST'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    flash(f'Author {author.name} and all their books deleted!', 'success')
    return redirect(url_for('home'))

# Route for AI-based book recommendation
@app.route('/recommend')
def recommend():
    books = Book.query.all()
    book_titles = [book.title for book in books]
    recommendation = get_book_recommendation(book_titles)
    return render_template('recommend.html', recommendation=recommendation)

def get_book_recommendation(book_titles):
    openai.api_key = app.config['OPENAI_API_KEY']
    prompt = f"Based on the following books: {', '.join(book_titles[:5])}, recommend a book."  # Limit titles to 5
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=50)
    return response.choices[0].text.strip()

# Route to display all books
@app.route('/all_books')
def all_books():
    books = Book.query.all()
    return render_template('all_books.html', books=books)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
