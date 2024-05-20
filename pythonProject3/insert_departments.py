import sqlite3 as lit
import xlsx_pull
import transliterate
import openpyxl


def xl_to_data(file='', n=0):

    '''запись таблицы категорий ( каждой группы каждого напраления )'''

    id = n
    books = openpyxl.open(file, read_only=True)
    sheet = books.active
    db = lit.connect('shedule.db')
    numbers = None
    faculties = None
    members = None
    for departments in sheet.iter_rows(min_row=3, min_col=5, max_row=5, values_only=True):
        if numbers is None:
            numbers = departments
            continue
        else:
            if faculties is None:
                faculties = departments
                continue
            else:
                members = departments

    for i in range(0,len(numbers)):
        id += 1
        if members[i] is None:
            print('finished')
            return True
        else:
            try:
                temp_information = numbers[i]
                dep_number = temp_information.split(' ')[0]
            except Exception:
                dep_number = 'no information'

            faculty = faculties[i]

            temp_group = members[i]
            slug_group = transliterate.translit(temp_group, reversed=True)

            new_group = (id, temp_group, slug_group, dep_number, faculty)

            print(new_group)

            with db:
                print(new_group)
                cur = db.cursor()
                cur.execute(f'INSERT INTO users VALUES (?,?,?,?,?)', new_group)
                new_group = 0

    print('data was fully inserted')

# fill up the data with
if __name__ == '__main__':
    xl_to_data('xlsx_pull/tech_y_trans.xlsx', )


