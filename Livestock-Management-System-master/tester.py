from backend import DataBase
import sqlite3
import datetime
from datetime import datetime, date

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('SELECT (julianday(:curdate) - julianday(:date_of_birth)) AS day WHERE day > 365 ', {'curdate': datetime.date(datetime.now()), 'date_of_birth': '2000-01-01'})
r = c.fetchall()

age = 'Kid' if len(r) == 0 else 'Adult'
category = age + ' Male' if False else age + ' Female'

c.execute('SELECT DISTINCT breed, category FROM LivestockNetworth')
res = c.fetchall()
print(type(res))

# print(category)
