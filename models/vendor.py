from app import db
from marshmallow import Schema, fields

class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

class VendorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

vendor_schema = VendorSchema()
