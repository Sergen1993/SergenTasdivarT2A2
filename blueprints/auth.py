from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import check_password_hash
from models.chef import Chef, ChefSchema

auth_bp = Blueprint('auth_bp', __name__)
chef_schema = ChefSchema()

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    chef = Chef.query.filter_by(email=email).first()
    if not chef or not check_password_hash(chef.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=chef.id)
    return jsonify({'access_token': access_token})

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    chef_id = get_jwt_identity()
    chef = Chef.query.get(chef_id)
    if not chef:
        return jsonify({'message': 'User not found'}), 404

    return chef_schema.jsonify(chef)
