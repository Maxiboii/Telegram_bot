#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telebot
import requests
import re
import sqlite3
import config
import getClasses
import getLinks
import time


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


#  filling the DB


def update_DB():
    one_inst = getClasses.Rozklad()
    x = one_inst.get_rozklad()

    conn = sqlite3.connect('rozklad.sqlite')
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS Classes''')

    cur.execute('''CREATE TABLE Classes
        (id INTEGER UNIQUE, week_No INTEGER, weekday TEXT, No INTEGER,
        tm TEXT, teacher TEXT, class TEXT, room TEXT, link TEXT)''')

    print('Filling the Databse')
    count_id = 0
    for dayk, day in x['week1'].items():
        w = 1
        subj_count = 1
        for subj in x['week1'][dayk]:
            if subj != '':
                print(subj)
                cur.execute('''INSERT OR IGNORE INTO Classes (id, week_No,
                weekday, No, tm, teacher, class, room)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (count_id, w, dayk,
                    subj_count, subj[0], subj[1], subj[2], subj[3]))
                count_id += 1
                print('Adding', subj)
            subj_count += 1


    for dayk, day in x['week2'].items():
        w = 2
        subj_count = 1
        for subj in x['week2'][dayk]:
            if subj != '':
                cur.execute('''INSERT OR IGNORE INTO Classes (id, week_No,
                weekday, No, tm, teacher, class, room)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (count_id, w, dayk,
                    subj_count, subj[0], subj[1], subj[2], subj[3]))
                count_id += 1
                print('Adding', subj)
            subj_count += 1


    conn.commit()
    conn.close()
    print('Database filled 50%')
    print('Might take a few minutes...')


    username = input('Enter username: ')
    password = input('Enter password: ')
    two_inst = getLinks.Google(username, password)
    two_inst.login()
    toa = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg0Nzk1NDgw')
    oke = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg5MzU4NTU1')
    angl = two_inst.get_link('https://classroom.google.com/u/1/c/MTU5MTk4NjIyMTA4')
    moac = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyOTA5NzE0MzM2')
    nastenka_lab = 'https://meet.google.com/jpt-hwcx-vbi'
    nastenka_pr = 'https://meet.google.com/esc-chjz-kan'
    schema = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyMDE1ODE3ODYz')
    tps = two_inst.get_link('https://classroom.google.com/u/1/c/MTQ4OTI1MjY2Njc1')
    two_inst.q()

    links = [toa, oke, oke, oke,
            toa, angl, moac,
            toa, schema, schema, schema,
            tps, tps, nastenka_lab,
            moac, oke, oke,
            toa, angl, moac,
            toa, schema, schema,
            tps, tps, nastenka_pr]

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


w1l = [[], [], [], [], []]
w2l = [[], [], [], [], []]
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


rasp = {'1': w1l, '2': w2l}


#  formatting


def get_mes(week, day):
    mes = ''
    mes += 'Тиждень ' + str(week) + ', ' + day + '\n'
    for i in rasp[str(week)]:
        for s in i:
            if day in s:
                mes += str(s[3]) + '.\t' + s[4] + ' ' + s[5] + ' ' + s[7].split()[1] + '\n' + s[6] + '\n' + '-  ' + s[8] + '\n\n'
    return mes


# commands
def start_command(bot, update):
    bot.send_message(
        update.message.chat.id,
        'Greetings! I help with giving you the schedule you need.\n\n' +
        "To get today's schedule use\n/chotamsednya.\n\n" +
        'To get schedule for tomorrow use\n/chotamzavtra.'
   )

def chotamsednya(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=get_mes(*what_is_today(time.strftime('%W'),
    time.strftime('%A')))
    )

def chotamzavtra(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=get_mes(*what_is_today(time.strftime('%W',
    time.localtime(time.time()+86400)), time.strftime('%A',
    time.localtime(time.time()+86400))))
    )

def update_DB1(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=update_DB())


#  run bot
def main():
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('chotamsednya', chotamsednya))
    dp.add_handler(CommandHandler('chotamzavtra', chotamzavtra))
    dp.add_handler(CommandHandler('update', update_DB1))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
