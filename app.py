from flask import Flask, jsonify, request as req
from flaskext.mysql import MySQL
from functools import wraps
from marshmallow import ValidationError

# Custom Functions
from db import MySQLConnection
from random_password_generator import random_password_generator
from schema import AddUser

app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL()
mysql.init_app(app)

# For random password generation on account creation
generate_password = random_password_generator()

def auth_wrapper(method):
	@wraps(method)
	def wrapper():
		# pass the type of user as an argument to the method
		# if the user has scope allow operation
		# else deny access
		pass

@app.route('/api/add', methods=['POST'])
def add_user():
	try:
		data = AddUser().load(req.get_json(force = True))
		print(data)
	except ValidationError as err:
		return jsonify(err.messages)
	except:
		return jsonify({'message': 'Error occured'})
	# print(f'incoming data: {data["type"]}')
	# print(generate_password())
	return jsonify({ 'status': 200, 'response': 'OK' })	

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
