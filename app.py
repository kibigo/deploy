from flask import Flask, make_response, request, jsonify, session
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import requests
import datetime
from flask_bcrypt import Bcrypt
import base64
from requests.auth import HTTPBasicAuth
from model import db, Customer, Product, Order, OrderItem, Favourite, Payment, Review, TopCategory, FeaturedBrands


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.json.compact = False

bcrypt = Bcrypt(app)

CORS(app, supports_credentials=True)

migrate = Migrate(app, db)

db.init_app(app)

class Register(Resource):

    @staticmethod
    def post():

        firstname = request.json['firstname']
        lastname = request.json['lastname']
        phone = request.json['phone']
        email = request.json['email']
        password = request.json['password']
     
        user = Customer.query.filter_by(email=email).first()

        if user:
            message = {
                "error":"User already exist"
            }
            response = make_response(
                jsonify(message)
            )
            return response
        else:
            hashed_password = bcrypt.generate_password_hash(password)

            new_user = Customer(
                firstname = firstname,
                lastname = lastname,
                phone = phone,
                email = email,
                password = hashed_password
            )

            db.session.add(new_user)
            db.session.commit()

            response = {
                "id":new_user.id,
                "firstname":new_user.firstname,
                "lastname":new_user.lastname,
                "phone":new_user.phone,
                "email":new_user.email,
                "is_admin":new_user.is_admin
            }

            return make_response(
                jsonify(response)
            )

api.add_resource(Register, '/register')


class Login(Resource):

    @staticmethod
    def post():
        email = request.json['email']
        password = request.json['password']

        user_existing = Customer.query.filter_by(email=email).first()

        if user_existing is None:
            message = {
                "error":"Unauthorized"
            }
            response = make_response(
                jsonify(message)
            )
            return response
        
        if not bcrypt.check_password_hash(user_existing.password, password):
            message = {
                "error":"Unauthorized"
            }
            response = make_response(
                jsonify(message)
            )
            return response
        
        session['user_id'] = user_existing.id
        
        response_data = {
            "id":user_existing.id,
            "name":user_existing.firstname,
            "email":user_existing.email,
            "is_admin":user_existing.is_admin
        }

        response = make_response(
            jsonify(response_data)
        )

        return response
    
api.add_resource(Login, '/login')


class Logout(Resource):

    @staticmethod
    def delete():
        session['user_id'] = None

        logout_message ={
            "message" : "You have been logged out"
        }

        response = make_response(
            jsonify(logout_message)
        )

        return response

api.add_resource(Logout, '/logout')



class GetUser(Resource):

    @staticmethod
    def get():
        user = session.get('user_id')

        user_details = Customer.query.filter_by(id=user).first()

        if user_details:
            response_data = {
                "id":user_details.id,
                "name":user_details.firstname,
                "email":user_details.email
            }
            response = make_response(
                jsonify(response_data)
            )

            return response
        
        else:
            return None
    
    

api.add_resource(GetUser, '/user')

class GetUserById(Resource):

    @staticmethod
    def get(id):
        single_user = Customer.query.filter_by(id = id).first()
        response_data = {
            "id":single_user.id,
            "firstname":single_user.firstname,
            "lastname":single_user.lastname,
            "phone":single_user.phone,
            "email":single_user.email,
            "password":single_user.password
        }
        response = make_response(
            jsonify(response_data)
        )
        return response
api.add_resource(GetUserById, '/user/<int:id>')

class GetProduct(Resource):

    @staticmethod
    def get():
        list = [item.to_dict() for item in Product.query.all()]

        response = make_response(
            jsonify(list)
        )

        return response

api.add_resource(GetProduct, '/products')

class Product_By_Category(Resource):

    @staticmethod
    def get():

        category_given = request.json['category']
        filtered_data = [item.to_dict() for item in Product.query.filter_by(category = category_given).all()]

        response = make_response(
            jsonify(filtered_data)
        )

        return response

api.add_resource(Product_By_Category, '/category')


class OrderClass(Resource):
    
    @staticmethod
    def post():
        user = session.get('user_id')
        name = request.json['name']
        county = request.json['county']
        street = request.json['street']

        if user is None:

            response = make_response(
                jsonify({"Error" : "User not authenticated"}),
                401
            )
            return response
        
        total_amount = request.json.get('amount')

        print("AMount received", user)

        if total_amount is None:

            response = make_response(
                jsonify({"error" : "Amount not provided"}),
                400
            )
            return response
        
        new_order = Order(
            user_id = user,
            name = name,
            county = county,
            street = street,
            total_amount = total_amount
        )

        db.session.add(new_order)
        db.session.commit()

        order_data = {
            "id":new_order.id,
            "user_id":new_order.user_id,
            "total_amount":new_order.total_amount
        }

        response = make_response(
            jsonify(order_data),
            201
        )

        return response
    
    @staticmethod
    def get():
        order_list = [item.to_dict() for item in Order.query.all()]
        response = make_response(
            jsonify(order_list)
        )
        return response

api.add_resource(OrderClass, '/orders')


class OrderById(Resource):

    @staticmethod
    def get(id):
        single_order = Order.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(single_order)
        )

        return response
    
    @staticmethod
    def patch(id):
        single_order = Order.query.filter_by(id=id).first()
        
        for attr in request.form:
            setattr(single_order, attr, request.form[attr])
        
        db.session.add(single_order)
        db.session.commit()

        response_dict = single_order.to_dict()

        response = make_response(
            jsonify(response_dict)
        )

        return response
    
    @staticmethod
    def delete(id):
        data = Order.query.filter_by(id=id).first()

        db.session.delete(data)
        db.session.commit()

        response_data = {
            "message":"Data deleted"
        }
        
        response = make_response(
            jsonify(response_data)
        )

        return response
    
api.add_resource(OrderById, '/orders/<int:id>')


class Topcategory(Resource):

    @staticmethod
    def get():
        item_list = [item.to_dict() for item in TopCategory.query.all()]

        response = make_response(
            jsonify(item_list)
        )
        return response

api.add_resource(Topcategory, '/topcategory')


class Featuredbrands(Resource):

    @staticmethod
    def get():
        item_list = [item.to_dict() for item in FeaturedBrands.query.all()]
        response = make_response(
            jsonify(item_list)
        )

        return response

api.add_resource(Featuredbrands, '/featuredbrands')

class Make_Payment(Resource):
    
    @staticmethod
    def post():

        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, required = True)
        parser.add_argument('amount', type=str, required=True)
        args = parser.parse_args()

        phone_number = args['phone']
        amount = args['amount']

        consumer_key ="haIzzoBjE6eUAGKu4J9vBvqrEL8l3Dm2"
        consumer_secret = "BCnrl9RpzVu19gM9"
        api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()

        access_token = "Bearer " + data['access_token']

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

        bussiness_shortcode = '174379'

        data_to_encode = bussiness_shortcode + passkey + timestamp

        encoded_data = base64.b64encode(data_to_encode.encode())

        password = encoded_data.decode('utf-8')

        request = {
            "BusinessShortCode": bussiness_shortcode,
            "Password": password,
            "Timestamp": timestamp, # timestamp format: 20190317202903 yyyyMMhhmmss 
            "TransactionType": "CustomerPayBillOnline",
            "Amount": round(float(amount)),
            "PartyA": f"254{phone_number[1:]}",
            "PartyB": bussiness_shortcode,
            "PhoneNumber": f"254{phone_number[1:]}",
            "CallBackURL": "https://mydomain.com/pat",
            "AccountReference": "Limited",
            "TransactionDesc": "Payment of Jackson"
        }

        stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        headers = {"Authorization": access_token, "Content-Type": "application/json"}

        #making STK push request

        response = requests.post(stk_url,json=request,headers=headers)

        if response.status_code > 299:
            mpesa_response = {
                'message':'Failed'
            }
            final_response = make_response(
                jsonify(mpesa_response)
            )

            return final_response
        else:
            message = {
                'message':'Successful'
            }
            response = make_response(
                jsonify(message)
            )

    
            new_data = Payment(
                phone = phone_number,
                amount = amount
            )

            db.session.add(new_data)
            db.session.commit()

            return response
        
        

api.add_resource(Make_Payment, '/make_payment')


class GetPayments(Resource):

    @staticmethod
    def get():
        payment_list = [pay.to_dict() for pay in Payment.query.all()]
        
        response_data = make_response(
            jsonify(payment_list)
        )

        return response_data

api.add_resource(GetPayments, '/payment')


if __name__ == '__main__':
    app.run(debug=True)