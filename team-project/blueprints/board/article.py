from flask import Blueprint, render_template, request

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.article import Article

article = Blueprint('article', __name__, url_prefix='/article')

@article.route('/<int:article_id>', methods=['GET'])
def index(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)

@article.route('/', methods=['POST'])
@jwt_required()
def create():
    return