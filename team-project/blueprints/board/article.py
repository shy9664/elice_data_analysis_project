from flask import Blueprint, render_template, request, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.article import Article

from app import db 

from datetime import datetime

article = Blueprint('article', __name__, url_prefix='/article')

@article.route('/<int:article_id>', methods=['GET'])
def index(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)

@article.route('/create', methods=['GET'])
def create_page():
    if request.method == 'GET':
        return render_template('article_form.html')

@article.route('/create', methods=['POST'])
@jwt_required()
def create():
    if request.method == 'POST':
        user_info = get_jwt_identity()
        user_id = user_info['user_id']
        name = request.json['name']
        title = request.json['title']
        content = request.json['content']
        new_article = Article(user_id, name, title, content, datetime.now())
        print(user_id, name, title, content)
        print(new_article)
        db.session.add(new_article)
        db.session.commit()
        return jsonify(result='success')