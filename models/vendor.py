from database import db

class Vendor(db.Model):
    __tablename__ = 'vendors'

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(500))
    email = db.Column(db.String(100), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'email': self.email
        }
