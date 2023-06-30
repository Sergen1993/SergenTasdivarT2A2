from flask import Blueprint, jsonify, request
from app import db
from models.order import Order, OrderSchema

order_bp = Blueprint('order_bp', __name__)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.jsonify(orders)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    item_id = request.json['item_id']
    quantity = request.json['quantity']
    chef_id = request.json['chef_id']

    new_order = Order(item_id, quantity, chef_id)

    db.session.add(new_order)
    db.session.commit()

    return order_schema.jsonify(new_order)

@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return order_schema.jsonify(order)

@order_bp.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    order.item_id = request.json.get('item_id', order.item_id)
    order.quantity = request.json.get('quantity', order.quantity)
    order.chef_id = request.json.get('chef_id', order.chef_id)

    db.session.commit()

    return order_schema.jsonify(order)

@order_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message': 'Order deleted'})
