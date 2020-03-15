# Application modules
from flask import Flask, jsonify, request as req, abort
from flaskext.mysql import MySQL
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt

# General modules
from functools import wraps

# Custom Functions
from db import MySQLConnection
from random_password_generator import random_password_generator
from schema import AddUser
from util import get_items, generate_placeholders

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL()
mysql.init_app(app)
bcrypt = Bcrypt(app)

# For random password generation on account creation
generate_password = random_password_generator()

def auth_wrapper(method):
	@wraps(method)
	def wrapper():
		# pass the type of user as an argument to the method
		# if the user has scope allow operation
		# NOTE: need to find whether it makes sense to pass the operation as argument
		# 			to the decorator is a good idea
		# else deny access
		pass

@app.route('/api/add', methods=['POST'])
def add_user():
	connection = None
	try:
		data = AddUser().load(req.get_json(force = True))
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
			# if bcrypt.check_password_hash(pw_hash, password):
			# 	print('Passwords match!!')
			login_query = "INSERT INTO EmployeeLogin VALUES ("+generate_placeholders(3)+")"
			cur.execute(login_query, (user_id, username, pw_hash))
			if user_type == 'admin':
				options['id'] = user_id
				keys, values = get_items(options)
				if len(keys):
					role_query = "INSERT INTO AdminInfo ("+keys+") VALUES ("+generate_placeholders(3)+")"
					cur.execute(role_query, values)
			elif user_type == 'manager':
				pass
			elif user_type == 'staff':
				pass
		connection.commit()
		return jsonify({ 'message': 'User Created' })
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
	# with MySQLConnection(mysql) as connection:
	# 	print('Connection Established')
	# print('connection closed')
	#cur.execute('''SELECt * FROM sample''')
	#r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	# r = {1: 1, 2: 2}
	# return jsonify({'data': r})
	return 'Hello There!'

if __name__ == '__main__':
	app.run()
