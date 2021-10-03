from flask import Blueprint, render_template, request, jsonify
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

        user = User(user_id, user_pw, name)
        
        db.session.add(user)
        db.session.commit()

        return jsonify({'result':'success'})