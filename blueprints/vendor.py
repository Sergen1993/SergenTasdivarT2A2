from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.vendor import Vendor, VendorSchema

vendor_bp = Blueprint('vendor_bp', __name__)
vendor_schema = VendorSchema()

@vendor_bp.route('/vendors', methods=['GET'])
@jwt_required()
def get_vendors():
    chef_id = get_jwt_identity()
    vendors = Vendor.query.filter_by(chef_id=chef_id).all()
    return vendor_schema.jsonify(vendors, many=True)

@vendor_bp.route('/vendors', methods=['POST'])
@jwt_required()
def create_vendor():
    chef_id = get_jwt_identity()
    name = request.json.get('name')
    address = request.json.get('address')

    if not name or not address:
        return jsonify({'message': 'Name and address are required'}), 400

    vendor = Vendor(chef_id=chef_id, name=name, address=address)
    db.session.add(vendor)
    db.session.commit()

    return jsonify({'message': 'Vendor created successfully!'})

# Other vendor routes...
