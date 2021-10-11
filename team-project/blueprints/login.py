from flask import Blueprint, render_template, request, jsonify

from flask_jwt_extended import create_access_token, get_csrf_token

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
            user_info = {'user_id': user.user_id, 'name': user.name}
            access_token_cookie = create_access_token(identity=user_info)
            csrf_access_token = get_csrf_token(access_token_cookie)
            res = jsonify(result='success', user_name=user.name, user_id=user.user_id, csrf_access_token=csrf_access_token)
            res.set_cookie('access_token_cookie', access_token_cookie, httponly=True)
            return res
        return jsonify({'result':'fail'})

