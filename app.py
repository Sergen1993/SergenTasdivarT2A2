from flask import Flask
from blueprints.chef_blueprint import chef_bp
from blueprints.inventory_blueprint import inventory_bp
from blueprints.order_blueprint import order_bp
from blueprints.vendor_blueprint import vendor_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(chef_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(order_bp)
app.register_blueprint(vendor_bp)

if __name__ == '__main__':
    app.run()
