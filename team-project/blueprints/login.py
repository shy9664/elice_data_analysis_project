from flask import Blueprint, render_template, request, jsonify, url_for, redirect

from app import db
from models.user import User

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']

        user = User.query.filter((User.user_id == user_id) & (User.user_pw == user_pw)).first()

        if user :
            return redirect(url_for('main.index', name=user.name))
        
        return jsonify({'result':'fail'})