from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.inventory_item import InventoryItem, InventoryItemSchema

inventory_bp = Blueprint('inventory_bp', __name__)
inventory_item_schema = InventoryItemSchema()

@inventory_bp.route('/inventory-items', methods=['GET'])
@jwt_required()
def get_inventory_items():
    chef_id = get_jwt_identity()
    inventory_items = InventoryItem.query.filter_by(chef_id=chef_id).all()
    return inventory_item_schema.jsonify(inventory_items, many=True)

@inventory_bp.route('/inventory-items', methods=['POST'])
@jwt_required()
def create_inventory_item():
    chef_id = get_jwt_identity()
    name = request.json.get('name')
    quantity = request.json.get('quantity')
    notes = request.json.get('notes', '')

    if not name or not quantity:
        return jsonify({'message': 'Name and quantity are required'}), 400

    inventory_item = InventoryItem(chef_id=chef_id, name=name, quantity=quantity, notes=notes)
    db.session.add(inventory_item)
    db.session.commit()

    return jsonify({'message': 'Inventory item created successfully!'})

# Other inventory item routes...
