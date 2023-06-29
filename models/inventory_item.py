from database import db

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(500))
    chef_id = db.Column(db.String(64), db.ForeignKey('chefs.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'notes': self.notes
        }
