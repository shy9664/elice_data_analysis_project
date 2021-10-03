from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from app import db
from models.user import User

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        name = request.form['name']
        user = User.query.filter(User.user_id == user_id).first()

        if not user:
            new_user = User(user_id, user_pw, name)
            
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('login.index'))

        return jsonify({'result': 'fail'})