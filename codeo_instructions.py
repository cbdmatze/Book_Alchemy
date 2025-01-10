'''
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                    🛫_Your own digital library 📚_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Are you the type of person who loves to keep their books displayed on a shelf? Or maybe you have so many books
    that you store them in boxes! Or, perhaps you're a person who prefers eBooks or listening to audio books.


🛫  No matter how you like to consume books, you would probably benefit from having an easily-accessible list of all the books
    you own or have read/listened to, as well as a list of their authors.


🛫  In this excercise, we'll create our own digital library using Flask and flask-sqlalchemy ro achieve that!


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                🛫_👩‍💻 Flask-SQLAlchemy library_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Flask-SQLAlchemy extends SQLAlchemy by providing additional integration specifically tailored for Flask applications.
    It simplifies the setup and configuration of SQLAlchemy within a Flask app, reducing the amount of boilerplate code required 
    to get started.


🛫  With flask-sqlalchemy, you can define your db.models as python classes, leveraging SQLAlchemy's ORM capabilities to easily 
    map these classes to db.tables.


🛫  Ready to go?

        >>> https://giphy.com/gifs/bbmas-billboard-music-awards-bbma-bbmas-2022-sl1zfWPqlozOgquzuE


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                            🛫_Step 1: Setup_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  📜 Documentation

    You will probably need to reference the flask-sqlalchemy documentation and/or the SQLAlchemy documentation 
    while you complete this exercise.

        >>> https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

        >>> https://docs.sqlalchemy.org/



🛫  🏗️ Setup

    _python_libraries_:

    >>> Install the flask, sqlalchemy, flask_sqlalchemy, and jinja2 libraries into your environment.


    _create_a_SQLite_file_:

    >>> Create a new SQLite file called 'library.sqlite' within the existing '/data' directory
    


    _initialize_the_Flask_app_:

    >>> create a file called 'app.py' in the project's root directory (at the same level as the 'data/' and 
        'templates/' directories).
        
    >>> import these packages at the top of 'app.py':

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
'''

    >>> create an instance of the Flask application after the imports.

'''
app = Flask(__name__)
'''


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                🛫_Step 2: Configure flask-sqlalchemy 🧪_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  The next thing we need to do is tell Flask where it van find our db. file.  
    To do that, let's briefly learn about db.URIs and then specify the db. URI for this project.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                    🛫_Setting the Database URI_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Configure the db. connection by specifying the db. 'Uniform Resource Identifier (URI) after the initialized Flask app in 'app.py', 
    which is a string that specifies the connection details and location of a db.

    It's commonly used to establish a connection between an application and a db. management system (DBMS). This 'URI' contains information
    such as the DBMS tyoe, host, port, db. name and authentication credentials.


🛫  For this demonstration we will be using an SQLite3 db. and we will set the db. URI as follows:


'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
'''


🛫  In the 'app.py' file, include the following imports. We haven't created these yet, but we will in the next section.


'''
from data_models import db, Author, Book
'''


🛫  Note that we import an object called 'db' form 'data_models.py'. Let's use that object in 'app.py'. 
    Add this line of code after the 'app.config()' line that was introduced earlier.


'''
db.init_app(app)
'''


🛫  This will connect the Flask app to the flask-sqlalchemy code.


🛫  Next, it's time to define some data models for our library!


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                            🛫_Step 3: Define the Author and Book models ✍_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Our digital library needs to store authors and books, at a minimum.



🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                            🛫_Create a Python file for the data classes_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a new python file called 'data_models.py'. This is the file you'll create the models in, which are listed below in 
    subsequent steps.


🛫  At the top of the file, add the following import and create a 'db' object:


'''
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
'''


🛫  Recall that we've already imported the 'db' object in the 'app.py' file. This means that your 'app.py' file now has access to the db.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                    🛫_👩‍🎓 Define the Author model_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a class called 'Author' that inherits from 'db.Model', inside the class, define the attributes 'id', 'name', birth_date', 
    and 'date_of_death'. The 'id' should be an 'auto-incrementing Primary Key (PK). Set the appropriate column types and constraints
    for each attribute.


🛫  Customize the string representation (optional): You can define custom '__repr__()' and '__str__()' methods to provide 
    a customized string representation of the 'Author' instance.

    
    str()

    Remember the __str__() magic method? It allows you to override the string representation for an object. 
    We covered it in a previous Academy Lesson here.


🛫  This is useful for debugging and displaying meaningful information about the object. This can be a very helpful step to take and is 
    generally considered as best practice.

                            📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖
    
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                    🛫_📖 Define a Book model_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

                            📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖📖

🛫  Define a 'Book' model that includes the properties 'id', 'isbn', 'title', and 'publication_year' as columns, using the 'Author' model
    you just wrote as a guide.

    Also add the 'author_id' as a Foreign Key to the 'Author' table, so the two tables can be conneted.


🛫  Optionally, customize the __repr__() and __str__() methods for the 'Book' class.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                    🛫_Create the new tables_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Once you've defined the 'Book' and the 'Author' tables, you'll need to run this code so that SQLAlchemy can create them for you:


'''
with app.app_context():
    db.create_all()
'''


🛫  You only need to run this code once, you can put it at the bottom of your file and then comment it out once you've run it.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                        🛫_Step 4: Create your library 📚_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  With the tables set up, let's now turn our attentin to the backend Flask routes. They will define the logic for adding authors
    and books to our library.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                            🛫_👩‍🎓 Add authors_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Before we can start adding books to the library, which is the ultimate goal, we need first to add their authors to the authors table
    because of the Foreign Key relationship.


🛫  First import your data models in the imports section of app.py.


🛫  Create a Flask route called '/add_author' that renders the 'add_authors.html' form used to gather information about an author
    when a GET request comes in, and adds a new author record to the database using SQLAlchemy when a POST request comes in.
    When a new author has successfully been added to the database, a success message should be displayed on the '/add_author' page.


🛫  Note that becausse you created an autoincrementing Primary Key for the 'id' column of the 'Author' mode, you don't need to show
    a text field in the form for the user to insert their own author 'id'.

                                    🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕
    
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                        🛫_🆕 Add books_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

                                    🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕

                                    
🛫  Now that we have a way to add authors, we can add books!


🛫  Create a Flask route called '/add_book' that renders a form in 'add_book.html' used to gather information about a book when a GET
    request comes in, and adds a new book record to the database when a POST request comes in.


🛫  You will need to add the necessary code to 'templates/add_book.html'. You can use the code your wrote for 'templates/add_author'
    as a guide. Add a dropdown menu so the user can select an author from a list of authors that have already been saved to the db.


🛫  Remember to show a success message on the '/add_book' page when a new book has successfully been added to the db.


🛫  Hint: You can use the Flask route you created for the '/add_book' page when a new book has successfully been added to the db.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                            🛫_🏡 Home page_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a Flask route for the home pag that queries the Book table and returns:

        1.  The 'render_template()' function for the 'home.html' template.

        2.  The books data returned by the database query, in a format the jinja code in the HTML file expects.


🛫  Enhance your homepage

        >>> Next to the book's title, also display its author. This is really easy using SQLAlchemy, because the 'Book' and the 
            'Author' models are connected.

        >>> Display each book's cover image alongside the book title. You could obtain the image using the ISBN and any external 
            API you would like to use. 



🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                        🛫_🌼 Seed some data_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Now that you have the 'Author' and 'Book' tables established, add 5-10 authors using your '/add_author' route, then 5-10 books
    using your '/add_book' route.


🛫  Did they apper as expected on your Home page?


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                            🛫_Enable Sorting_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a way for the books shown on the home page to be sorted. You could add buttons or a dropdown to your HTML file, and/or
    a new Flask route that handles sorting the books. At a minimum, the books should be sortable by 'title' and by 'author_name'.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                            🛫_Step 5: Keyword Search_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


        Keyword Search 📚

        >>> Let's add the ability to search our 'Book' table for a word or phrase, like in the case where we want to 
            display a specific book without having to scroll through all the books in order to find it.

        >>> Add a small text field form to your 'home.html' template. Clicking the "Search" button (which you will also 
            need to add) should cause the Flask route to run a query using 'flask_sqlalchemy' that uses the text input
            in the HTML form as a string query in the 'flask_sqlalchemy' query. This is aikin to using the 'LIKE' 
            keyword in SQL.

        >>> The Flask route should either render all the books that meet the search criteria, or it should somehow
            display a message that says there were no books that match the search criteria.

            
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                            🛫_Step 6: Time to donate? ♻_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  No one carries a book around with them forever. We eventually need to let go of some of our books, and gifting them
    to others or donating them to your local library are great options for downsizing your library!
    Whenb you give away books, you'll need to remove them from your digital library.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                            🛫_❎ Delete a Book_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a route called '/book/<int:book_id>/delete' which deletes a specific book from the db. when a POST request
    comes in. Redirect the user to the homepage (the "Library") after a successful deletion, and display a success 
    message indicating that the deletion of the book worked as required.


🛫  Add a "Delete Book" button to 'home.html', so a user can easily delete a book from the homepage. If the book's author
    doesn't have any other books in your library, you can also delete the author from your db.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                                🛫_Bonus ✨_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Woo hoo, you did it! 🌟 You created a Flask application and connected it to a SQLite database 
    using SQLAlchemy!


🛫  Here are some fun bonus exercises you can complete if you’d like to extend the capabilities 
    of your library application. You can do one, some, or all of them.



🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                🛫Bonus #1 - Use ChatGPT to Redesign the UI 🤖__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  In the recent live codeint session with your Schoolmaster, you learned about using ChatGfPT to redesign the UI
    of a website. Implement what you learned on your digital library app.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                        🛫_Bonus #2 - Detail Pages 🔎_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  It would be nice to be able to click on a book title on your homepage and view details about the book in a 
    new page.


🛫  Define a Flask route and create HTML pages that render detail pages for books and authors. Retrieve the relevant
    data from the db. based on the provided author/book_id, then dynamically generate the content for each page.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                        🛫_Bonus #3 - Delete an Author ❌_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a route called '/author/<int:author_id>/delete' which deletes a specific author from the db. when a POST request
    comes in. Redirect the user to the homepage (the "Library") after a successful deletion, and display a success message
    indicatin that the deletion of the author worked.


🛫  Add a "Delete Author" button to 'home.html'. It should appear underneath of next to each author's name, and it should 
    delete ALL books in your db. with Foreign Keys to that author. When you refresh the HTML page, those books should no 
    longer appear in your digital library.


🛫  Suppose you delete a row from a table that contains a column that is a Foreign Key to another table. In our case, 
    this would happen when you delete a row from the 'Book' table because it contains a Foreign Key column to the 
    'Author' table.


🛫  You get to decide how to handle the data that exists in the table that contains the Foreign Key; in our example, you 
    get to decide how to handle the author data when deleting a book. the choices vary a bit depending on the db. your're 
    using, but generally, you can delete the author, protect the author from being deleted, or update the author value
    to something else.


🛫  this decision can be specified with SQLAlchemy using the 'cascade=all' feature. You can look this up in the 
    'flask_sqlalchemy' and/or the 'SQLALchemy' documentation.

    
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                        🛫_Bonus #4 - Book Ratings 🥇_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Add functionality so you can provide a rating (1-10) for each book in your library.


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
                                🛫_Bonus #5 - Suggest a Book to Read 💡_🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫  Create a page that uses Artificial Intelligence to generate a book recommendation based on the books in your library, 
    and that optionally takes into account your book ratings (if you completed the Bonus #3 above).


🛫  The Flask route should send all the books that the user has read to 'ChatGPT', and let 'ChatGPT' generate a recommendation.
    You could find a free 'AI API' to use on

            >>> RapidApi (look for any ChatGPT that allows a free plan with a hard limit).


🛫 


🛫 


🛫 

🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 

🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 


🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
🛫__🛫 
🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 🛫 
'''