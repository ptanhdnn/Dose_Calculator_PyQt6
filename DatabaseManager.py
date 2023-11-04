import os
import sqlite3

class Database():
    def __init__(self) -> None:
        # self.name = name
        pass


    def createDatabase(self):
        # Connect to the database
        os.mkdir('')
        os.chdir('Databases')
        connect = sqlite3.connect('database.db')
        c = connect.cursor()

        # Tạo bảng lưu danh sách khách hàng
        c.execute('''CREATE TABLE IF NOT EXISTS CustomerPackage (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Company TEXT NOT NULL,
            PackageType TEXT NOT NULL
        )''')

        # Tạo bảng lưu lịch sử chiếu xạ
        c.execute('''CREATE TABLE IF NOT EXISTS DoseCustomer (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT NOT NULL,
            Company TEXT NOT NULL,
            PackageType TEXT NOT NULL,
            Quantity INTEGER,
            DoseRequired REAL,
            IrradiationTime TEXT,
            Note TEXT
        )''')
        # # Insert a row into the database
        # c.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', ('John Doe', 'john.doe@example.com'))
        connect.commit()
        connect.close()
        os.chdir('..')

    def insertCustomerPackage(self, companyName, packName):
        connect = sqlite3.connect('Databases/database.db')
        c = connect.cursor()
        c.execute('''INSERT INTO CustomerPackage (Company, PackageType) VALUES (?, ?)''', (companyName, packName))
        connect.commit()
        connect.close()

    def insertDoseCustomer(self, date, companyName, packName, quantity, doseRequired, irradiationTime, note):
        connect = sqlite3.connect('Databases/database.db')
        c = connect.cursor()
        c.execute('''INSERT INTO DoseCustomer (Date, Company, PackageType, Quantity, DoseRequired, IrradiationTime, Note) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                              (date, companyName, packName, quantity, doseRequired, irradiationTime, note))
        connect.commit()
        connect.close()