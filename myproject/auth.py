from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Check if the user actually exists
    # Take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # If the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    
    # Validate and add user to database 
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    fav_food = request.form.get('fav_food')

    user = User.query.filter_by(email=email).first() # If this returns a user, then the email already exists in database

    if user: # If a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists') # May not want to show this to users. Security risk!
        return redirect(url_for('auth.signup'))

    # Create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name,fav_food=fav_food, password=generate_password_hash(password, method='sha256'))

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
