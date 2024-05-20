import sqlite3 as lit
import openpyxl
import xlsx_pull


def xl_to_shedule(file='', n=0):

    '''запись данных расписания факультета в таблицу юазы данных'''

    id = n
    books = openpyxl.open(file)
    sheet = books.active
    db = lit.connect('shedule.db')
    for all_groups in sheet.iter_cols(min_col=5, min_row=6, max_row=58, values_only=True):
        id += 1
        with db:
            day_of_the_week('monday', 0, 8, all_groups, db, id)
            day_of_the_week('tuesday', 9, 17, all_groups, db, id)
            day_of_the_week('wednesday', 18, 26, all_groups, db, id)
            day_of_the_week('thursday', 27, 35, all_groups, db, id)
            day_of_the_week('friday', 36, 44, all_groups, db, id)
            day_of_the_week('saturday', 45, 53, all_groups, db, id)


def day_of_the_week(day_of_the_week, start_pos, finish_pos, all_groups, db, id):

    '''фильтрация данных на тип *название пары*|*вид занятия*|*номер аудитории*
    с учетом исключений некоректности общедоступного расписания рудн'''

    exceptions = ['     /', '  ', '   ', '    ', '                  ', 'г', "\\"]
    cur = db.cursor()
    i = start_pos
    print(all_groups[start_pos:finish_pos])
    day = [id, ]
    while i < finish_pos:
        flag = 0
        temp = all_groups[i]
        if temp in exceptions or temp is None:
            temp = 'нет пары'
            day.append(temp)
            i += 1
        elif temp[:2] == 'МД' or temp[:2] == 'МП':
            day.append(temp)
            i += 1
        elif '/' in temp[:5]:
            day.append('нет пары')
            i += 1
        elif '/' in temp:
            if temp[-1] == '/':
                temp = temp[0:-1]
                if ';' in temp:
                    splitted_temp = temp.split(';')
                    flag = 1
                else:
                    day.append(temp)
                    i += 1
                    flag = 0
            else:
                try:
                    chet, nechet = temp.split('/')
                except Exception:
                    temp = temp.replace('п/г','')
                    chet, nechet = temp.split('/')
                splitted_temp = chet.split(';')
                flag = 1
        else:
            splitted_temp = temp.split(';')
            flag = 1

        '''нормальный вид записи данных ниже, выше исключения'''

        if flag == 1 and len(splitted_temp) >= 2:
            for ind in range(1, len(splitted_temp)):
                if '1' or '2' or '3' or '4' or '5' or '6' or '7' in splitted_temp[ind]:
                    try:
                        day.append(splitted_temp[0] + '|' + splitted_temp[ind] + '|' + splitted_temp[ind+2])
                    except IndexError:
                        day.append(splitted_temp[0] + '|' + splitted_temp[ind])
                    splitted_temp = []
                    i += 1
                    break
                else:
                    day.append(splitted_temp[0] + '|' + splitted_temp[1])
                    i += 1
        elif flag == 1 and len(splitted_temp) == 1:
            day.append(temp)
            i += 1
    print(day)
    cur.execute(f'INSERT INTO {day_of_the_week} VALUES (?,?,?,?,?,?,?,?,?)', day)


if __name__ == '__main__':
    xl_to_shedule('xlsx_pull/tech_y_trans.xlsx', 99)
