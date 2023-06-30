from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.order import Order, OrderSchema

order_bp = Blueprint('order_bp', __name__)
order_schema = OrderSchema()

@order_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    chef_id = get_jwt_identity()
    orders = Order.query.filter_by(chef_id=chef_id).all()
    return order_schema.jsonify(orders, many=True)

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    chef_id = get_jwt_identity()
    inventory_item_id = request.json.get('inventory_item_id')
    quantity = request.json.get('quantity')

    order = Order(chef_id=chef_id, inventory_item_id=inventory_item_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()

    return jsonify({'message': 'Order created successfully!'})

# Other order routes...
