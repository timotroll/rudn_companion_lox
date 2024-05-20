import sqlite3 as lit
import os

import openpyxl

'''создание таблицы ( сугубо столбцов ) направлений и групп'''

def main():
    try:
        db = lit.connect('shedule.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE users (id INTEGER, name TEXT, slug TEXT, dep_number TEXT, faculty TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Table")


if __name__ == "__main__":
    main()