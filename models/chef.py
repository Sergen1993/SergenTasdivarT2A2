from werkzeug.security import generate_password_hash, check_password_hash
from database import db

class Chef(db.Model):
    __tablename__ = 'chefs'

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Relationships
    inventory_items = db.relationship('InventoryItem', backref='chef', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
