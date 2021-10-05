from flask import Blueprint, render_template, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, decode_token

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@main.route('/', methods=['POST'])
@jwt_required()
def analyze():
    if request.method == 'POST':
        return jsonify(result='success')
