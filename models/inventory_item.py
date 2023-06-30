from app import db
from marshmallow import Schema, fields, validate

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    chef_id = db.Column(db.Integer, db.ForeignKey('chefs.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    def __init__(self, chef_id, name, quantity, notes=None):
        self.chef_id = chef_id
        self.name = name
        self.quantity = quantity
        self.notes = notes

class InventoryItemSchema(Schema):
    id = fields.Int(dump_only=True)
    chef_id = fields.Int(required=True)
    name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    notes = fields.Str()

inventory_item_schema = InventoryItemSchema()
