# Application modules
from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
import jwt

# General modules
from functools import wraps
from datetime import datetime, timedelta

# Custom Functions
from db import MySQLConnection
from random_password_generator import random_password_generator
from schema import AddUser, UserLogin
from util import get_items, generate_placeholders

# creating instance of the Flask class
app = Flask(__name__)

app.config.from_pyfile('config.py')
mysql = MySQL()
mysql.init_app(app)
bcrypt = Bcrypt(app)

# For random password generation on account creation
generate_password = random_password_generator()

def auth_wrapper(method):
	@wraps(method)
	def wrapper(*args, **kwargs):
		access_token = request.headers.get('jwt-auth-token')
		try:
			payload = jwt.decode(access_token.encode('utf-8'), app.config['TOKEN_KEY'], algorithms='HS256')
			username = payload['username']
			current_user = None
			with MySQLConnection(mysql) as connection:
				with connection.cursor() as cur:
					get_user = "SELECT username, id FROM EmployeeLogin WHERE username = %s"
					cur.execute(get_user, username)
					fetched_username, current_user = cur.fetchall()[0]
					if not fetched_username:
						raise Exception('Invalid Token')
			return method(current_user_id=current_user, *args, **kwargs)
		except jwt.exceptions.ExpiredSignatureError as e:
			return jsonify({ 'message': 'Session Expired' }), 403
		except Exception as e:
			print('Error:', e)
			return jsonify({ 'message': 'Forbidden' }), 403
	return wrapper

@app.route('/api/login', methods=['POST'])
def login():
	try:
		data = UserLogin().load(request.get_json(force = True))
		username, password = data['username'], data['password']
		with MySQLConnection(mysql) as connection:
			with connection.cursor() as cur:
				get_password = "SELECT password FROM EmployeeLogin WHERE username = %s"
				cur.execute(get_password, username)
				password_hash = cur.fetchall()[0][0]
				if not password_hash or not bcrypt.check_password_hash(password_hash, password):
					raise Exception('Invalid Credentials')
					pass
		payload = { 'username': username, 'exp': datetime.utcnow() + timedelta(minutes=5) }
		token = jwt.encode(payload, app.config['TOKEN_KEY'], algorithm='HS256')
		# print(token, token.decode('utf-8').encode('utf-8'))
		return jsonify({ 'access_token': token.decode('utf-8') })
	except Exception as e:
		print('Error:', e)
		return jsonify({ 'message': 'Authentication Error' }), 401

@app.route('/api/add', methods=['POST'])
@auth_wrapper
def add_user(current_user_id):
	connection = None
	try:
		data = AddUser().load(request.get_json(force = True))
		if data.get('options', None):
			options = data['options']
			del data['options']
		username, email, user_type = data['username'], data['email'], data['user_type']
		del data['username']
		del data['user_type']
		keys, values = get_items(data)
		# Add added by user to the data by getting from authentication
		connection = mysql.connect()
		with connection.cursor() as cur:
			detail_query = "INSERT INTO EmployeeDetails ("+keys+") VALUES ("+generate_placeholders(len(values))+")"
			cur.execute(detail_query, values)
			cur.execute("SELECT id FROM EmployeeDetails WHERE email=%s", (email))
			user_id = cur.fetchall()[0][0]
			password = generate_password()
			pw_hash = bcrypt.generate_password_hash(password)
			login_query = "INSERT INTO EmployeeLogin VALUES ("+generate_placeholders(3)+")"
			cur.execute(login_query, (user_id, username, pw_hash))
			if user_type == 'admin':
				keys, values = get_items(options)
				# dont insert another primary user if one is already present
				if len(keys):
					keys+=', id'
					values.append(user_id)
					role_query = "INSERT INTO AdminInfo ("+keys+") VALUES ("+generate_placeholders(len(values))+")"
					cur.execute(role_query, values)
			elif user_type == 'manager':
				pass
			elif user_type == 'staff':
				pass
		connection.commit()
		return jsonify({ 'message': 'User Created' }), 201
	except ValidationError as err:
		return jsonify({ 'message': err.messages }), 400
	except Exception as err:
		if connection:
			connection.rollback()
		print("Unexpected error:", err)
		return jsonify({ 'message': 'Cannot process request' }), 500
	finally:
		if connection:
			connection.close()

@app.route('/', methods=['GET'])
def home():
	return 'Hello There!'

if __name__ == '__main__':
	app.run()
