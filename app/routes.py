from flask import Blueprint, render_template, request, redirect, url_for
from .extensions import db
from .models import User

app = Blueprint('app', __name__)

@app.route('/')
def index():
    users_count = User.query.count()
    active_users_count = User.query.count()  # placeholder for demo
    return render_template('index.html', users_count=users_count, active_users_count=active_users_count)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('app.view_users'))
    return render_template('add_user.html')

@app.route('/view_users')
def view_users():
    users = User.query.all()
    return render_template('view_users.html', users=users)
