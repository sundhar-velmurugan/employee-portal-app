from flask import Flask, jsonify
from flaskext.mysql import MySQL
from db import MySQLConnection

app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def get():
	with MySQLConnection(mysql) as connection:
		print('Connection Established')
	print('connection closed')
	#cur.execute('''SELECt * FROM sample''')
	#r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	# r = {1: 1, 2: 2}
	# return jsonify({'data': r})
	return 'Hello There!'

if __name__ == '__main__':
	app.run()
