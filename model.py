from flask_sqlalchemy import SQLAlchemy
import re
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String, nullable = False)
    lastname = db.Column(db.String, nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    email= db.Column(db.String, unique = True)
    password = db.Column(db.String, nullable = False)
    is_admin = db.Column(db.Boolean, default = False, nullable = False)
    created_at = db.Column(db.DateTime(), server_default = db.func.now())

    order = db.relationship('Order', backref = 'customer_orders', lazy = True)
    favourite = db.relationship('Favourite', backref='customer_favourites', lazy = True)

    def __repr__(self):
        return f"Name: {self.firstname} {self.lastname}"
    
    @validates("firstname", "lastname")
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name field cannot be empty')
        return name
    
    @validates("email")
    def validate_email(self, key, email):
        pattern = r'^\S+@\+\.\S+$'
        if re.search(pattern, email):
            raise ValueError("Invalid email")
        return email
    
class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    category = db.Column(db.String, nullable = False)
    weight = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    imageurl = db.Column(db.String, nullable = False)

    favourite = db.relationship('Favourite', backref='product_favourites', lazy = True)
    review = db.relationship('Review', backref='product_reviews', lazy = True)

    def __repr__(self):
        return f"Name: {self.name}"
    
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name cannot be empty')
        return name

class TopCategory(db.Model, SerializerMixin):
    __tablename__ = 'topcategories'

    id = db.Column(db.Integer, primary_key = True)
    imageurl = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"Name: {self.name}"

class FeaturedBrands(db.Model, SerializerMixin):
    __tablename__ = 'featuredbrands'

    id = db.Column(db.Integer, primary_key = True)
    imageurl = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"Name: {self.name}"



class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    county = db.Column(db.String)
    street = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    total_amount = db.Column(db.Float)
    order_date = db.Column(db.DateTime(), server_default = db.func.now())

    orderItem = db.relationship('OrderItem', backref='order_orderItems', lazy = True)
    payment = db.relationship('Payment', backref='order_payments', lazy = True, foreign_keys = 'Payment.order_id')

    def __repr__(self):
        return f"Total: {self.total_amount}"


class OrderItem(db.Model, SerializerMixin):
    __tablename__ = "orderItems"

    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)

class Favourite(db.Model, SerializerMixin):
    __tablename__ = "favourites"

    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self) -> str:
        return f"Product_id: {self.product_id}"

class Payment(db.Model, SerializerMixin):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    phone = db.Column(db.Integer)
    payment_date = db.Column(db.DateTime(), server_default=db.func.now())
    amount = db.Column(db.Integer, db.ForeignKey('orders.total_amount'))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())

    def __repr__(self) -> str:
        return f"Amount paid: {self.amount}"
    
class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
