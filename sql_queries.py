import sqlite3
conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()
# Запитання 1. Інформація про скількох художників представлена у базі даних?
# cursor.execute("SELECT * FROM artists")

# Запитання 2. Скільки жінок (Female) у базі?
# cursor.execute("SELECT * FROM artists WHERE Gender == \"Female\"")

# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
# cursor.execute("SELECT * FROM artists WHERE \"Birth Year\"<1900")

# Запитання 4*. Як звати найстаршого художника?
cursor.execute("SELECT Name FROM artists ORDER BY \"Birth Year\"")
data=cursor.fetchall()
print(data[0])