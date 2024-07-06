import wget

'''имопрт данных с сайта рудн в виде xlsx таблиц для дальнейшей обработки'''

energ_machin = 'https://esystem.rudn.ru/upload2/735693d96813a3c18d40ce28e02b128c'
nanotech = 'https://esystem.rudn.ru/upload2/04d087cd614112b6619f11073dd586e8'
inno_manage = 'https://esystem.rudn.ru/upload2/32e6b86c954cb5b3316040100bdd73a3'
meh_upr_proces = 'https://esystem.rudn.ru/upload2/18328b3fd62df07b2314e2e234ea335b'
neftegaz = 'https://esystem.rudn.ru/upload2/895ec03351e9bc279976c51bcd0d1007'
machin_stroy = 'https://esystem.rudn.ru/upload2/3f6b89ede348a9caeb2de297c4f6dddb'
tech_y_trans = 'https://esystem.rudn.ru/upload2/b9881c2bdca9a20d6cb081a21391d02b'
tech_stroy = 'https://esystem.rudn.ru/upload2/7f7800ac604396841bdf92c2eaca41ec'
architecht = 'https://esystem.rudn.ru/upload2/08cc5dc4b71816d326888181d3e57863'

wget.download(energ_machin, 'energ_machin.xlsx')
wget.download(nanotech, 'nanotech.xlsx')
wget.download(inno_manage, 'inno_manage.xlsx')
wget.download(meh_upr_proces, 'meh_upr_proces.xlsx')
wget.download(neftegaz, 'neftegaz.xlsx')
wget.download(machin_stroy, 'machin_stroy.xlsx')
wget.download(tech_y_trans, 'tech_y_trans.xlsx')
wget.download(tech_stroy, 'tech_stroy.xlsx')
wget.download(architecht, 'architecht.xlsx')