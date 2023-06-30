from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from models import db
from blueprints.auth import auth_bp
from blueprints.inventory import inventory_bp
from blueprints.vendor import vendor_bp
from blueprints.order import order_bp

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Initialize JWT
jwt = JWTManager(app)

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(vendor_bp)
app.register_blueprint(order_bp)

# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'message': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run()
