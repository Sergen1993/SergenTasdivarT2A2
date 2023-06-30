from flask import Blueprint, jsonify, request
from app import db
from models.vendor import Vendor, VendorSchema

vendor_bp = Blueprint('vendor_bp', __name__)

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)

@vendor_bp.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return vendors_schema.jsonify(vendors)

@vendor_bp.route('/vendors', methods=['POST'])
def create_vendor():
    name = request.json['name']
    address = request.json.get('address', None)

    new_vendor = Vendor(name, address)

    db.session.add(new_vendor)
    db.session.commit()

    return vendor_schema.jsonify(new_vendor)

@vendor_bp.route('/vendors/<int:id>', methods=['GET'])
def get_vendor(id):
    vendor = Vendor.query.get(id)
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404
    return vendor_schema.jsonify(vendor)

@vendor_bp.route('/vendors/<int:id>', methods=['PUT'])
def update_vendor(id):
    vendor = Vendor.query.get(id)
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404

    vendor.name = request.json.get('name', vendor.name)
    vendor.address = request.json.get('address', vendor.address)

    db.session.commit()

    return vendor_schema.jsonify(vendor)

@vendor_bp.route('/vendors/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    vendor = Vendor.query.get(id)
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404

    db.session.delete(vendor)
    db.session.commit()

    return jsonify({'message': 'Vendor deleted'})
