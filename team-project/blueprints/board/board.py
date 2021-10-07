from flask import Blueprint, render_template, request, jsonify

from models.article import Article

from flask_jwt_extended import jwt_required

board = Blueprint('board', __name__, url_prefix='/board')

@board.route('/')
def index():
    article_list = Article.query.order_by(Article.create_date.desc()).all()
    return render_template('board.html', article_list=article_list)

@board.route('/create', methods=['GET', 'POST'])
@jwt_required()
def create():
    if request.method == 'GET':
        return jsonify(result='success')