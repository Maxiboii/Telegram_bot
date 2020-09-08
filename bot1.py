from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import sqlite3
import config
import getClasses
import getLinks
import time


time_in_sec = time.time()
today_week_number = time.strftime('%W')
today_weekday = time.strftime('%A')
tomorrow_week_number = time.strftime('%W', time.localtime(time_in_sec+86400))
tomorrow_weekday = time.strftime('%A', time.localtime(time_in_sec+86400))

wd_translation = {
'Monday': 'Понеділок',
'Tuesday': 'Вівторок',
'Wednesday': 'Середа',
'Thursday': 'Четвер',
'Friday': "П'ятниця",
'Saturday': 'Субота',
'Sunday': 'Неділя'
}

def what_is_today(twn, twd):
    if int(twn) % 2 == 1:
        current_week = 1
        return (current_week, wd_translation[twd])
    else:
        current_week = 2
        return (current_week, wd_translation[twd])


### filling the DB
def update_DB():
    one_inst = getClasses.Rozklad()
    x = one_inst.get_rozklad()

    conn = sqlite3.connect('rozklad.sqlite')
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS Classes''')

    cur.execute('''CREATE TABLE Classes
        (id INTEGER UNIQUE, week_No INTEGER, weekday TEXT, No INTEGER, class TEXT, link TEXT)''')

    print('Filling the Databse')
    count_id = 0
    for dayk, day in x['week1'].items():
        w = 1
        subj_count = 1
        for subj in x['week1'][dayk]:
            if subj != '':
                cur.execute('''INSERT OR IGNORE INTO Classes (id, week_No, weekday, No, class)
                    VALUES ( ?, ?, ?, ?, ? )''', ( count_id, w, dayk, subj_count, subj ))
                count_id += 1
                print('Adding', subj)
            subj_count += 1


    for dayk, day in x['week2'].items():
        w = 2
        subj_count = 1
        for subj in x['week2'][dayk]:
            if subj != '':
                cur.execute('''INSERT OR IGNORE INTO Classes (id, week_No, weekday, No, class)
                    VALUES ( ?, ?, ?, ?, ? )''', ( count_id, w, dayk, subj_count, subj ))
                count_id += 1
                print('Adding', subj)
            subj_count += 1


    conn.commit()
    conn.close()
    print('Database filled 50%')
    print('Might take a few minutes...')

    two_inst = getLinks.Google(getLinks.username, getLinks.password)
    two_inst.login()
    toa = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg0Nzk1NDgw')
    oke = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg5MzU4NTU1')
    angl = 'вона нас не любить :с'
    moac = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyOTA5NzE0MzM2')
    schema = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyMDE1ODE3ODYz')
    tps = two_inst.get_link('https://classroom.google.com/u/1/c/MTQ4OTI1MjY2Njc1')
    two_inst.q()

    links = [toa,oke,oke,oke,toa,angl,moac,toa,schema,schema,schema,
            tps,tps,moac,moac,oke,oke,toa,angl,moac,toa,schema,schema,tps,tps,moac]

    conn = sqlite3.connect('rozklad.sqlite')
    cur = conn.cursor()

    print('Filling the Databse')
    l_count = 0
    for i in links:
        print('Adding', i)
        cur.execute("UPDATE Classes SET link = ? WHERE id = ?", (i, l_count))
        l_count += 1


    conn.commit()
    conn.close()
    print('Database filled succesfully')
    return 'Database filled, succesfull update'





# one_inst = getClasses.Rozklad()
#
# two_inst = getLinks.Google(getLinks.username, getLinks.password)
# two_inst.login()
# toa = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg0Nzk1NDgw')
# moac = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyOTA5NzE0MzM2')
# two_inst.q()
# print(toa)
# print(moac)
#
# links = [toa, '', moac]


# database
conn = sqlite3.connect('rozklad.sqlite')
cur = conn.cursor()

rozkladData_lst_y = list()
rozkladData_lst = list()
rozkladData_dic = {}

rozkladData = cur.execute('SELECT * FROM Classes')
all_subj = []
for x in rozkladData:
    y = str(x[1]) + ' ' + x[2]
    rozkladData_lst_y.append(y)
    rozkladData_lst.append(x)

kilkist = {}
for den in rozkladData_lst_y:
    kilkist[den] = rozkladData_lst_y.count(den)


w1l = [[],[],[],[],[]]
w2l = [[],[],[],[],[]]
for para, kolichestvo in kilkist.items():
    quan_ls = list(kilkist.values())
    if para == '1 Понеділок':
        for i in range(kolichestvo):
            w1l[0].append(rozkladData_lst[i])
    elif para == '1 Вівторок':
        for i in range(sum(quan_ls[:1]), sum(quan_ls[:1]) + kolichestvo):
            w1l[1].append(rozkladData_lst[i])
    elif para == '1 Середа':
        for i in range(sum(quan_ls[:2]), sum(quan_ls[:2]) + kolichestvo):
            w1l[2].append(rozkladData_lst[i])
    elif para == '1 Четвер':
        for i in range(sum(quan_ls[:3]), sum(quan_ls[:3]) + kolichestvo):
            w1l[3].append(rozkladData_lst[i])
    elif para == "1 П'ятниця":
        for i in range(sum(quan_ls[:]), sum(quan_ls[:]) + kolichestvo):
            w1l[4].append(rozkladData_lst[i])
    elif para == '2 Понеділок':
        for i in range(sum(quan_ls[:4]), sum(quan_ls[:4]) + kolichestvo):
            w2l[0].append(rozkladData_lst[i])
    elif para == '2 Вівторок':
        for i in range(sum(quan_ls[:5]), sum(quan_ls[:5]) + kolichestvo):
            w2l[1].append(rozkladData_lst[i])
    elif para == '2 Середа':
        for i in range(sum(quan_ls[:6]), sum(quan_ls[:6]) + kolichestvo):
            w2l[2].append(rozkladData_lst[i])
    elif para == '2 Четвер':
        for i in range(sum(quan_ls[:7]), sum(quan_ls[:7]) + kolichestvo):
            w2l[3].append(rozkladData_lst[i])
    elif para == "2 П'ятниця":
        for i in range(sum(quan_ls[:]), sum(quan_ls[:]) + kolichestvo):
            w2l[4].append(rozkladData_lst[i])


da_suka = {'1': w1l, '2': w2l}

######formatting

def get_mes(week, day):
    mes = ''
    mes += 'Тиждень ' + str(week) + ', ' + day + '\n'
    for i in da_suka[str(week)]:
        for s in i:
            if day in s:
                mes += str(s[3]) + '.\t' + (str(s[4]) + '\n') + '-  ' + s[5] + '\n\n'
    return mes


def chotamsednya(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text = get_mes(*what_is_today(today_week_number, today_weekday)))

def chotamzavtra(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text = get_mes(*what_is_today(tomorrow_week_number, tomorrow_weekday)))

def update_DB1(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text = update_DB())

######### run bot

def main():
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('chotamsednya',chotamsednya))
    dp.add_handler(CommandHandler('chotamzavtra',chotamzavtra))
    dp.add_handler(CommandHandler('update',update_DB1))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
