import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE country")

cursor.execute("CREATE TABLE country (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO country VALUES (1, 'China')")
cursor.execute("INSERT INTO country VALUES (2, 'USA')")
cursor.execute("INSERT INTO country VALUES (3, 'UK')")
cursor.execute("INSERT INTO country VALUES (4, 'U')")
cursor.execute("INSERT INTO country VALUES (5, 'AU')")
conn.commit()

print("=======before delete=======")
countries = cursor.execute("SELECT * FROM country").fetchall()
for country in countries:
    print(country)

cursor.execute("UPDATE country SET name='Unite State' WHERE name='USA'")

# cursor.execute("DELETE FROM country WHERE name like '%U'")
#
print("=======after delete=======")
countries = cursor.execute("SELECT * FROM country").fetchall()
for country in countries:
    print(country)