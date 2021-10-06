from flask import Blueprint, render_template, request

from models.article import Article

board = Blueprint('board', __name__, url_prefix='/board')

@board.route('/')
def index():
    article_list = Article.query.order_by(Article.create_date.desc()).all()
    return render_template('board.html', article_list=article_list)