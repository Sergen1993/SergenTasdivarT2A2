from app import db
from marshmallow import Schema, fields

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    chef_id = db.Column(db.Integer, db.ForeignKey('chefs.id'), nullable=False)
    inventory_item_id = db.Column(db.Integer, db.ForeignKey('inventory_items.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, chef_id, inventory_item_id, quantity):
        self.chef_id = chef_id
        self.inventory_item_id = inventory_item_id
        self.quantity = quantity

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    chef_id = fields.Int(required=True)
    inventory_item_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

order_schema = OrderSchema()
