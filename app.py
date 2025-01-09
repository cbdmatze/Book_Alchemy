from flask import Flask, render_template, request, redirect, url_for, flash
from data_models import db, Author, Book
from forms import AddAuthorForm, AddBookForm
from utils import fetch_book_cover


app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)


# Route to add an author
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        new_author = Author(name=form.name.data, birth_date=form.birth_date.data)
        db.session.add(new_author)
        db.session.commit()
        flash('Author added successfully!', 'success')
        return redirect(url_for('add_author'))
    return render_template('add_author_html', form=form)


# Route to add a book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    if form.validate_on_submit():
        cover_url = fetch_book_cover(form.isbn.data) # Get cover image from external API
        new_book = Book(
            title=form.title.data, 
            isbn=form.isbn.data,
            cover_url=cover_url,
            author_id=form.author.data
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('add_book'))
    return render_template('add_book.html', form=form)


# Route to display books on the home page
@app.route('/')
def home():
    sort_by = request.args.get('sort_by', 'title') # Default sort by title
    if sort_by == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.order_by(Book.title).all()
    return render_template('home.html', books=books)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
