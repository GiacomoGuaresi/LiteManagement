# app/routes/__init__.py
from flask import Blueprint

from app.routes.home import home_bp
from app.routes.bom import bom_bp
from app.routes.production import production_bp
from app.routes.progress import progress_bp
from app.routes.product import product_bp
from app.routes.inventory import inventory_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(bom_bp)
    app.register_blueprint(production_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(inventory_bp)
