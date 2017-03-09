import sqlite3
from forcast import fetchWeather, sortData

def creatDB():
	'''create database (if not exists)'''
	conn = sqlite3.connect('weather.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS data
		(date, city, weather, temp, wind)''')
	c.execute('DELETE FROM data')
	conn.commit()
	conn.close()

def getOne(key):
	'''fetch & sort weather of a city from api'''
	data = fetchWeather(key, 1)

	if 'status' in data:
		return 'none'
	else:
		a = sortData(data, key, 1)
		return a[0].split(' ')

def insertOne(a):
	'''insert into database'''
	conn = sqlite3.connect('weather.db')
	c = conn.cursor()
	c.execute('INSERT INTO data VALUES(?, ?, ?, ?, ?)', a)
	conn.commit()
	conn.close()
	print('successfully inserted')

def selectOne(key):
	'''select one item from database'''
	conn = sqlite3.connect('weather.db')
	c = conn.cursor()
	i = (key, )
	c.execute('SELECT * FROM data WHERE city=?', i)
	return c.fetchone()
	conn.commit()
	conn.close()

if __name__ == '__main__':
	creatDB()
	key = '杭州'
	a = getOne(key)
	print(a)
	insertOne(a)
	print(selectOne(key))

