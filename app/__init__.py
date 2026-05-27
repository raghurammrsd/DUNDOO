from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .config import Config
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "user.login"


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    
    with app.app_context():
        from app.models import User, Shopkeeper, Product, Order

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    from app.main.routes import main_bp
    from app.user.routes import user_bp
    from app.shop.routes import shop_bp
    from app.ai.routes import ai_bp
    from app.reels.routes import reels_bp

    app.register_blueprint(reels_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(shop_bp, url_prefix="/shop")
    app.register_blueprint(ai_bp)

    
    app.config["RAZORPAY_KEY_ID"] = os.getenv("RAZORPAY_KEY_ID")
    app.config["RAZORPAY_KEY_SECRET"] = os.getenv("RAZORPAY_KEY_SECRET")

    if not app.config["RAZORPAY_KEY_ID"]:
        raise RuntimeError("RAZORPAY_KEY_ID missing in environment")

    return app
