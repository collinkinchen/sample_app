from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, fav_food=current_user.fav_food)

@main.route('/food')
def food():
    return render_template('food.html', food_count=1, fav_food=current_user.fav_food)

@main.route('/update_count', methods=['POST'])
@login_required
def update_count():
    data = request.form.get('food_count')
    print(data)
    # return render_template('profile.html', name=current_user.name, fav_food=current_user.fav_food)
    return render_template('food.html', food_count=int(data)+1, fav_food=current_user.fav_food)
