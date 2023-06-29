from flask import Blueprint, request, jsonify
from models.order import Order
from models.vendor import Vendor
from models.chef import Chef
from database import db

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        vendor = Vendor.query.get(data['vendor_id'])
        chef = Chef.query.get(data['chef_id'])
        if vendor and chef:
            order = Order(vendor=vendor, chef=chef)
            db.session.add(order)
            db.session.commit()
            return jsonify(message='Order created successfully'), 201
        return jsonify(message='Vendor or chef not found'), 404
    except KeyError:
        return jsonify(message='Invalid payload'), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(message='Database error occurred'), 500

@order_bp.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify(order.serialize())
    return jsonify(message='Order not found'), 404

