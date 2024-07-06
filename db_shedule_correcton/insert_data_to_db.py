import sqlite3 as lit
import pandas as pd
import numpy as np
# import sys
# import os

# sys.path.insert(1, os.path.abspath('shedule_pull'))
# import shedule_pull


def xl_to_shedule(file=''):

    '''запись данных расписания факультета в таблицу юазы данных'''
    db = lit.connect('shedule.db')
    excel = pd.read_excel(file, skiprows=4)
    for index in range(4, excel.shape[1]):
        print('Column Number : ', index)

        # Select column by index position using iloc[]
        columnSeriesObj = excel.iloc[:, index]
        print(index)
        Chet, NeChet = ColumnToData(columnSeriesObj)
        ChetDict = []
        NeChetDict = []
        for keys, values in Chet.items():
            ChetDict.append(values)
        for keys, values in NeChet.items():
            NeChetDict.append(values)
        print(ChetDict)
        with db:
            cur = db.cursor()
            cur.execute('INSERT INTO chet VALUES (?,?,?,?,?,?,?)', ChetDict)
            cur.execute('INSERT INTO nechet VALUES (?,?,?,?,?,?,?)', NeChetDict)

def ColumnToData(columnSeriesObj):
    monday = columnSeriesObj[0:8]
    tuesday = columnSeriesObj[9:17]
    wednesday = columnSeriesObj[18:26]
    thursday = columnSeriesObj[27:35]
    friday = columnSeriesObj[36:44]
    saturday =columnSeriesObj[45:53]
    week = [monday, tuesday, wednesday, thursday, friday, saturday]
    DayIndex = 1
    Chet = {
        'GroupName': columnSeriesObj.name,
        'ChetMonday':'',
        'ChetTuesday':'',
        'ChetWednesday':'',
        'ChetThursday':'',
        'ChetFriday':'',
        'ChetSaturday':''
    }
    NeChet = {
        'GroupName': columnSeriesObj.name,
        'NeChetMonday': '',
        'NeChetTuesday': '',
        'NeChetWednesday': '',
        'NeChetThursday': '',
        'NeChetFriday': '',
        'NeChetSaturday': ''
    }
    for day in week:
        TempDayChet = ''
        TempDayNeChet = ''
        for pare in day:
            ChetPare, NeChetPare = PareToData(pare)
            TempDayChet = TempDayChet + '####' + ChetPare
            TempDayNeChet = TempDayNeChet + '####' + NeChetPare
        if DayIndex == 1:
            Chet['ChetMonday'] = TempDayChet
            NeChet['NeChetMonday'] = TempDayNeChet
        if DayIndex == 2:
            Chet['ChetTuesday'] = TempDayChet
            NeChet['NeChetTuesday'] = TempDayNeChet
        if DayIndex == 3:
            Chet['ChetWednesday'] = TempDayChet
            NeChet['NeChetWednesday'] = TempDayNeChet
        if DayIndex == 4:
            Chet['ChetThursday'] = TempDayChet
            NeChet['NeChetThursday'] = TempDayNeChet
        if DayIndex == 5:
            Chet['ChetFriday'] = TempDayChet
            NeChet['NeChetFriday'] = TempDayNeChet
        if DayIndex == 6:
            Chet['ChetSaturday'] = TempDayChet
            NeChet['NeChetSaturday'] = TempDayNeChet
        DayIndex += 1

    return Chet, NeChet


def PareToData(pare):

    '''фильтрация данных на тип *название пары*|*вид занятия*|*номер аудитории*
    с учетом исключений некоректности общедоступного расписания рудн'''
    exceptions = ['     /', '  ', '   ', '    ', '                  ', 'г', "\\"]
    if pare in exceptions or pare is None or type(pare) is float:
        ChetPare = 'нет пары'
        NeChetPare = 'нет пары'
        return ChetPare, NeChetPare
    elif pare[:2] == 'МД' or pare[:2] == 'МП':
        ChetPare = pare
        NeChetPare = pare
        return ChetPare, NeChetPare
    elif '/' in pare:
        if pare[-1] == '/':
            pare = pare[0:-1]
            if ';' in pare:
                splitted_pare = pare.split(';')
                pare = CheckForVals(splitted_pare)
                ChetPare = pare
                NeChetPare = 'нет пары'
                return ChetPare, NeChetPare
            else:
                ChetPare = pare
                NeChetPare = 'нет пары'
                return ChetPare, NeChetPare
        elif pare[0] == '/':
            pare = pare[1:]
            if ';' in pare:
                splitted_pare = pare.split(';')
                pare = CheckForVals(splitted_pare)
                ChetPare = 'нет пары'
                NeChetPare = pare
                return ChetPare, NeChetPare
            else:
                ChetPare = 'нет пары'
                NeChetPare = pare
                return ChetPare, NeChetPare
        else:
            try:
                chet, nechet = pare.split('/')
            except Exception:
                pare = pare.replace('п/г','')
                chet, nechet = pare.split('/')
            splitted_pare = chet.split(';')
            ChetPare = CheckForVals(splitted_pare)
            splitted_pare = nechet.split(';')
            NeChetPare = CheckForVals(splitted_pare)
            return ChetPare, NeChetPare
    else:
        splitted_pare = pare.split(';')
        pare = CheckForVals(splitted_pare)
        ChetPare = pare
        NeChetPare = pare
        return ChetPare, NeChetPare



def CheckForVals(splitted_pare):
    if len(splitted_pare) >= 2:
        for ind in range(1, len(splitted_pare)):
            if '1' or '2' or '3' or '4' or '5' or '6' or '7' in splitted_pare[ind]:
                try:
                    pare = splitted_pare[0] + '|' + splitted_pare[ind] + '|' + splitted_pare[ind+2]
                except IndexError:
                    pare = splitted_pare[0] + '|' + splitted_pare[ind]
                return pare
            else:
                pare = splitted_pare[0] + '|' + splitted_pare[1]
                return pare
    elif len(splitted_pare) == 1:
        return splitted_pare[0]

if '__main__' == __name__:
    xl_to_shedule('architecht.xlsx')
    xl_to_shedule('energ_machin.xlsx')
    xl_to_shedule('inno_manage.xlsx')
    xl_to_shedule('machin_stroy.xlsx')
    xl_to_shedule('meh_upr_proces.xlsx')
    xl_to_shedule('nanotech.xlsx')
    xl_to_shedule('neftegaz.xlsx')
    xl_to_shedule('tech_stroy.xlsx')
    xl_to_shedule('tech_y_trans.xlsx')
