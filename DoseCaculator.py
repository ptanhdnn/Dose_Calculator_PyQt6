import os
import PyQt6
import sqlite3
import sqlite3

from DatabaseManager import Database
db = Database()
if not os.path.exists('Databases/database.db'):
    print("database chưa được tạo!!!")
    db.createDatabase()
    print("Đã tạo database~~~")
else:
    print("database có tồn tại!!!")

db.insertCustomerPackage("Hải Thanh", "Thủy sản đông lạnh")

connect = sqlite3.connect('Databases/database.db')
c = connect.cursor()
c.execute('SELECT * FROM CustomerPackage')
result = c.fetchall()
print(result, type(result))

for row in result:
    print(row)

connect.close()
print("it ok now")