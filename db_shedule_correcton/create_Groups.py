import sqlite3 as lit
import os


'''создание таблицы ( сугубо столбцов ) направлений и групп'''

def CreateGroups():
    try:
        db = lit.connect('shedule.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE groups (id INTEGER, name TEXT, slug TEXT, dep_number TEXT, faculty TEXT)"

        cur.execute(tablequery)
        print("Table Groups Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Groups Table")

def CreateShedule():
    try:
        db = lit.connect('shedule.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE shedule (group_id INTEGER, chet INTEGER, nechet INTEGER)"

        cur.execute(tablequery)
        print("Table Shedule Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Shedule Table")

def CreateChetWeek():
    try:
        db = lit.connect('shedule.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE chet (group_name TEXT, monday TEXT, tuesday TEXT, wednesday TEXT, thursday TEXT, friday TEXT, saturday TEXT)"

        cur.execute(tablequery)
        print("Table Chet Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Chet Table")

def CreateNechetWeek():
    try:
        db = lit.connect('shedule.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE nechet (group_name TEXT, monday TEXT, tuesday TEXT, wednesday TEXT, thursday TEXT, friday TEXT, saturday TEXT)"

        cur.execute(tablequery)
        print("Table Nechet Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Nechet Table")

if __name__ == "__main__":
    CreateGroups()
    CreateShedule()
    CreateChetWeek()
    CreateNechetWeek()