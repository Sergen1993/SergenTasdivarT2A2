from flask import Blueprint, request, jsonify
from models.vendor import Vendor
from database import db

vendor_bp = Blueprint('vendor', __name__)

@vendor_bp.route('/vendors', methods=['POST'])
def create_vendor():
    try:
        data = request.json
        vendor = Vendor(name=data['name'], address=data['address'], email=data['email'])
        db.session.add(vendor)
        db.session.commit()
        return jsonify(message='Vendor created successfully'), 201
    except KeyError:
        return jsonify(message='Invalid payload'), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(message='Database error occurred'), 500

@vendor_bp.route('/vendors/<vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    vendor = Vendor.query.get(vendor_id)
    if vendor:
        return jsonify(vendor.serialize())
    return jsonify(message='Vendor not found'), 404

