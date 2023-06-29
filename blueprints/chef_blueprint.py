from flask import Blueprint, request, jsonify
from models.chef import Chef
from database import db

chef_bp = Blueprint('chef', __name__)

@chef_bp.route('/chefs', methods=['POST'])
def create_chef():
    try:
        data = request.json
        chef = Chef(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(chef)
        db.session.commit()
        return jsonify(message='Chef created successfully'), 201
    except KeyError:
        return jsonify(message='Invalid payload'), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(message='Database error occurred'), 500

@chef_bp.route('/chefs/<chef_id>', methods=['GET'])
def get_chef(chef_id):
    chef = Chef.query.get(chef_id)
    if chef:
        return jsonify(chef.serialize())
    return jsonify(message='Chef not found'), 404

# Add other chef routes for update, delete, and additional operations
