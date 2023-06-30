from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.Config')

# Initialize database
db = SQLAlchemy(app)

# Initialize database migrations
migrate = Migrate(app, db)

# Initialize JWT manager
jwt = JWTManager(app)

# Import blueprints
from app.blueprints.inventory.routes import inventory_bp
from app.blueprints.vendor.routes import vendor_bp
from app.blueprints.order.routes import order_bp
from app.blueprints.auth.routes import auth_bp

# Register blueprints
app.register_blueprint(inventory_bp, url_prefix='/inventory')
app.register_blueprint(vendor_bp, url_prefix='/vendor')
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(auth_bp, url_prefix='/auth')

# Run the Flask app
if __name__ == '__main__':
    app.run()
