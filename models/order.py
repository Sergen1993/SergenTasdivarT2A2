from database import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.String(64), primary_key=True)
    chef_id = db.Column(db.String(64), db.ForeignKey('chefs.id'), nullable=False)
    vendor_id = db.Column(db.String(64), db.ForeignKey('vendors.id'), nullable=False)

    chef = db.relationship('Chef', backref='orders', lazy=True)
    vendor = db.relationship('Vendor', backref='orders', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'chef_id': self.chef_id,
            'vendor_id': self.vendor_id
        }
