import sqlite3
from flask import Flask
from flask import request
from flask import render_template
from database import creatDB, getOne, insertOne, selectOne

app = Flask(__name__)
listH = []

@app.route('/', methods=['POST', 'GET'])
def interaction():
	conn = sqlite3.connect('weather.db')
	c = conn.cursor()

	if request.method == 'POST':
		listA = []
		key = request.form['key']
		i = (key, )
		c.execute('SELECT EXISTS(SELECT 1 FROM data WHERE city=?)', i)

		if c.fetchone() == (1, ):
			a = selectOne(key)
			return render_template('main.html',
				city=a[1], weather=a[2],
				temp=a[3], wind=a[4])
		else:
			a = getOne(key)

			if a == 'none':
				return render_template('main.html',
					weather='No result. Need Help?')
			else:
				listH.append(' '.join(a))
				insertOne(a)
				return render_template('main.html',
					city=a[1], weather=a[2],
					temp=a[3], wind=a[4])

	elif request.method == 'GET':

		if request.args.get('button') == 'Help':
			return render_template('main.html',
				help=' ')
		elif request.args.get('button') == 'History':
			return render_template('main.html',
				history=set(listH))
		else:
			return render_template('main.html')		

if __name__ == '__main__':
	creatDB()
	app.run('host=0.0.0.0')
