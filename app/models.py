from datetime import datetime
from flask_login import UserMixin
from app import db



class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(20))
    password_hash = db.Column(db.String(255), nullable=False)
    email_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    



class Shopkeeper(db.Model):
    __tablename__ = "shopkeepers"

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(100), nullable=False)
    shopkeeper_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    landmark = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    



class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    shopkeeper_id = db.Column(
        db.Integer,
        db.ForeignKey("shopkeepers.id"),
        nullable=False,
    )

    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    
    
    category = db.Column(db.String(50))

    price = db.Column(db.Numeric(10, 2))
    quantity = db.Column(db.Integer, default=0)

    
    opening_stock = db.Column(db.Integer, default=0)
    added_stock = db.Column(db.Integer, default=0)
    damaged_stock = db.Column(db.Integer, default=0)
    low_stock_threshold = db.Column(db.Integer, default=10)
    expiry_date = db.Column(db.Date, nullable=True)

    
    cost_price = db.Column(db.Numeric(10, 2))

    available = db.Column(db.Boolean, default=True)
    image_filename = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

   
    shop = db.relationship("Shopkeeper", backref="products")





class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)

    shopkeeper_id = db.Column(
        db.Integer,
        db.ForeignKey("shopkeepers.id"),
        nullable=False,
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
    )

    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)

    customer_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship("Product", backref="sales")
    shopkeeper = db.relationship("Shopkeeper", backref="sales")





class OTPRequest(db.Model):
    __tablename__ = "otp_requests"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    otp_code = db.Column(db.String(6), nullable=False)
    context = db.Column(db.String(50), nullable=False)
    payload = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)




class StockMovement(db.Model):
    __tablename__ = "stock_movements"

    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey("shopkeepers.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    change_type = db.Column(db.String(10))  
    quantity = db.Column(db.Integer, nullable=False)
    unit_cost = db.Column(db.Numeric(10, 2)) 
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship("Product")
    shop = db.relationship("Shopkeeper", backref="stock_moves")



class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey("shopkeepers.id"), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(50))
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    shop = db.relationship("Shopkeeper", backref="expenses")
    
class OnlineTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer)
    razorpay_order_id = db.Column(db.String(120))
    razorpay_payment_id = db.Column(db.String(120))
    amount = db.Column(db.Float)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class LoyaltyPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile = db.Column(db.String(15), unique=True)
    points = db.Column(db.Integer, default=0)


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey("shopkeepers.id"), nullable=False)

    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Float)

    status = db.Column(db.String(30), default="Placed")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="orders")
    product = db.relationship("Product")
    shopkeeper = db.relationship("Shopkeeper")
