from flask import Flask
from config import Config
from app.extensions import db, ma 
from app.routes.todos import todos_bp

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(todos_bp)
    
    with app.app_context():
        db.create_all()
        
    return app