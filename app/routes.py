from flask import render_template, flash, request, redirect, session
from app import create_app
from app.forms import *
from app.models import User, Book, Borrow, Category, db
from sqlalchemy.exc import IntegrityError

app = create_app()

@app.route("/sign_up",  methods=["GET", "POST"])
def sign_up():
    form  = SignUpForm(request.form)

    if form.validate_on_submit():
        password = str(form.password.data).strip()

        if ((password == str(form.confirm_password.data)) and len(password) > 1):
            user = User(username=str(form.username.data), password=password)
            db.session.add(user)

            try:
                db.session.commit()

                # after signup, redirect user to login page
                flash("Thanks for creating an account. Please login.")
                return redirect('/sign_in')
            except IntegrityError:
                flash("A user already exists with that username")
                return redirect('/sign_up')

        else:
            flash('password was either less than 5 character or wasn\'t equal')
            return render_template('sign_up.html', form=form)
    return render_template('sign_up.html', form=form)

@app.route("/sign_in",  methods=["POST", "GET"])
def sign_in():
    form = SignInForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(
            username=str(form.username.data),
            password=str(form.password.data)
        ).first()
        if user:

            # add user to session
            session["user_id"] = user.id

            flash("You logged in successfully")
            return redirect('/')
        else:
            flash("Your username or password was incorrect")
            return render_template('sign_in.html', form=form)
    return render_template('sign_in.html', form=form)


@app.route("/sign_out", methods=['GET'])
def logout():
    del session["user_id"]
    return redirect("/")


@app.route('/')
def home():
    user = get_current_user()
    if user:
        categories = Category.query.all()
        if user.admin:
            books = Book.query.all()
            return render_template('admin.html', user=user, categories=categories, books=books)
        else:
            borrows = user.borrows.filter_by(returned=False).all()
            for borrow in borrows:
                borrow.book = Book.query.filter_by(id=borrow.book_id).first()
            return render_template('user.html', user=user, categories=categories, borrows=borrows)

    # if user is logged out, render public page
    return render_template('index.html')


@app.route('/new-category', methods=['POST'])
def new_category():

    category = Category(title=request.form['title'])

    db.session.add(category)
    db.session.commit()

    flash('Successfully created category!')
    return redirect('/')

@app.route('/new-book', methods=['POST'])
def new_book():

    book = Book(title=request.form['title'], category_id=int(request.form['category_id']))

    db.session.add(book)
    db.session.commit()

    flash('Successfully added book!')
    return redirect('/')

@app.route('/new-borrow/<int:book_id>', methods=['GET'])
def new_borrow(book_id):

    user = get_current_user()
    borrow = Borrow.query.filter_by(user_id=user.id, book_id=book_id, returned=False).first()
    if borrow:
        flash('You have already borrowed that book.')
        return redirect('/')

    borrow = Borrow(user_id=user.id, book_id=book_id, returned=False)
    db.session.add(borrow)
    db.session.commit()

    flash('Successfully borrowed book!')
    return redirect('/')

@app.route('/new-return/<int:borrow_id>', methods=['GET'])
def new_return(borrow_id):

    borrow = Borrow.query.filter_by(id=borrow_id).first()
    if not borrow:
        flash('You did not borrow that book!')
        return redirect('/')

    borrow.returned = True

    db.session.add(borrow)
    db.session.commit()

    flash('Successfully returned book!')
    return redirect('/')

# func to return the current logged in user
def get_current_user():
    # user is logged in, if their id is in session
    is_logged_in = 'user_id' in session
    if not is_logged_in:
        return
    # if logged in,
    # query user record from db
    return User.query.filter_by(id=session['user_id']).first()
