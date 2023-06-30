from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models.chef import Chef, ChefSchema

chef_bp = Blueprint('chef_bp', __name__)
chef_schema = ChefSchema()

@chef_bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    chef = Chef.query.filter_by(email=email).first()
    if chef:
        return jsonify({'message': 'Email already registered'}), 400

    hashed_password = generate_password_hash(password)
    chef = Chef(email=email, password=hashed_password)
    db.session.add(chef)
    db.session.commit()

    return jsonify({'message': 'Chef registered successfully!'})

@chef_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    chef = Chef.query.filter_by(email=email).first()
    if not chef or not check_password_hash(chef.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate JWT token
    # ...

    return jsonify({'message': 'Logged in successfully!', 'token': '...'})

@chef_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_chef_profile():
    chef_id = get_jwt_identity()
    chef = Chef.query.get(chef_id)
    return chef_schema.jsonify(chef)

# Other chef-related routes...
