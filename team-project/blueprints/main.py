from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/', methods=['POST'])
@jwt_required()
def analyze():
    jwt = get_jwt_identity()
    if jwt:
        return jsonify(result='success', jwt=jwt)
    else:
        return jsonify(result='fail')
