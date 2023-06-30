from app import db
from marshmallow import Schema, fields

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    chef_id = db.Column(db.Integer, db.ForeignKey('chefs.id'), nullable=False)

    def __init__(self, name, quantity, price, chef_id):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.chef_id = chef_id

class InventoryItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)
    chef_id = fields.Int(required=True)
