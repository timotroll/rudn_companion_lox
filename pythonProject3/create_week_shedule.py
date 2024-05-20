import sqlite3 as lit

'''создание таблицы ( сугубо столбцов ) расписания каждой группы каждого направления'''
def make_day_of_the_week(day=''):
    try:
        db = lit.connect('shedule.db')
        cur = db.cursor()
        tablequery = f"CREATE TABLE {day} (id INTEGER, first TEXT, second TEXT, third TEXT, forth TEXT, fifth TEXT, sixth TEXT, seventh TEXT, eighth TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Table")


'''разделение на дни недели для упрощения прочитывания данных'''

if __name__ == "__main__":
    make_day_of_the_week('monday')
    make_day_of_the_week('tuesday')
    make_day_of_the_week('wednesday')
    make_day_of_the_week('thursday')
    make_day_of_the_week('friday')
    make_day_of_the_week('saturday')