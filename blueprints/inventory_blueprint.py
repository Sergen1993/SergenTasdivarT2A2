from flask import Blueprint, request, jsonify
from models.inventory_item import InventoryItem
from database import db

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/inventory', methods=['POST'])
def create_inventory_item():
    try:
        data = request.json
        item = InventoryItem(name=data['name'], quantity=data['quantity'], notes=data['notes'])
        db.session.add(item)
        db.session.commit()
        return jsonify(message='Inventory item created successfully'), 201
    except KeyError:
        return jsonify(message='Invalid payload'), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(message='Database error occurred'), 500

@inventory_bp.route('/inventory/<item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = InventoryItem.query.get(item_id)
    if item:
        return jsonify(item.serialize())
    return jsonify(message='Inventory item not found'), 404


