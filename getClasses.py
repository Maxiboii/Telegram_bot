#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
from time import sleep


class Rozklad:

    def __init__(self, group = 'дг-81'):
        self.group = group

        # selenium stuff
        # self.driver=webdriver.Chrome('/Users/Max/Desktop/Code/Selenium/chromedriver')
        # self.driver.get('http://rozklad.kpi.ua')
        # sleep(4)
        # self.driver.find_element_by_xpath('//*[@id="ctl00_lBtnSchedule"]').click()
        # sleep(1)
        # inpt = self.driver.find_element_by_xpath('//*[@id="ctl00_MainContent_ctl00_txtboxGroup"]')
        # inpt.send_keys(self.group)
        # inpt.send_keys(Keys.RETURN)

    def get_rozklad(self):

        url = 'http://rozklad.kpi.ua/Schedules/ViewSchedule.aspx?g=89a385d9-a264-4981-aa91-d7e12eb14730'
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")

        w1 = soup('table')[0]
        w2 = soup('table')[1]
        week1 = {}
        week2 = {}
        rozklad = {'week1': week1, 'week2': week2}

        mon = [x for x in w1.tr.next_siblings]
        mon.remove(mon[-1])
        mon1, zzl = [], []
        for x in mon:
            counter = 0
            sub = x.td.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    mon1.append(tuple(zzl))
                    zzl = []

        tue = [x for x in w1.tr.next_siblings]
        tue.remove(tue[-1])
        tue1, zzl = [], []
        for x in tue:
            counter = 0
            sub = x.td.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    tue1.append(tuple(zzl))
                    zzl = []

        wed = [x for x in w1.tr.next_siblings]
        wed.remove(wed[-1])
        wed1, zzl = [], []
        for x in wed:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    wed1.append(tuple(zzl))
                    zzl = []

        thu = [x for x in w1.tr.next_siblings]
        thu.remove(thu[-1])
        thu1, zzl = [], []
        for x in thu:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    thu1.append(tuple(zzl))
                    zzl = []

        fri = [x for x in w1.tr.next_siblings]
        fri.remove(fri[-1])
        fri1, zzl = [], []
        for x in fri:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    fri1.append(tuple(zzl))
                    zzl = []

        sat = [x for x in w1.tr.next_siblings]
        sat.remove(sat[-1])
        sat1, zzl = [], []
        for x in sat:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    sat1.append(tuple(zzl))
                    zzl = []
        wd1 = [mon1, tue1, wed1, thu1, fri1, sat1]

        mon = [x for x in w2.tr.next_siblings]
        mon.remove(mon[-1])
        mon1, zzl = [], []
        for x in mon:
            counter = 0
            sub = x.td.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    mon1.append(tuple(zzl))
                    zzl = []

        tue = [x for x in w2.tr.next_siblings]
        tue.remove(tue[-1])
        tue1, zzl = [], []
        for x in tue:
            counter = 0
            sub = x.td.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    tue1.append(tuple(zzl))
                    zzl = []

        wed = [x for x in w2.tr.next_siblings]
        wed.remove(wed[-1])
        wed1, zzl = [], []
        for x in wed:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    wed1.append(tuple(zzl))
                    zzl = []

        thu = [x for x in w2.tr.next_siblings]
        thu.remove(thu[-1])
        thu1, zzl = [], []
        for x in thu:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    thu1.append(tuple(zzl))
                    zzl = []

        fri = [x for x in w2.tr.next_siblings]
        fri.remove(fri[-1])
        fri1, zzl = [], []
        for x in fri:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    fri1.append(tuple(zzl))
                    zzl = []

        sat = [x for x in w2.tr.next_siblings]
        sat.remove(sat[-1])
        sat1, zzl = [], []
        for x in sat:
            counter = 0
            sub = x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')
            if sub != []: zzl.append(x.td.text[1:])
            for i in sub:
                counter += 1
                zzl.append(i.text)
                if counter == 3:
                    sat1.append(tuple(zzl))
                    zzl = []
        wd2 = [mon1, tue1, wed1, thu1, fri1, sat1]

        weekdays = []
        for weekday in w2.tr.td.next_siblings:
            weekdays.append(weekday)
        weekdays.remove(weekdays[-1])
        weekdays = [i.contents[0] for i in weekdays]
        count_z1 = 0
        for weekday in weekdays:
            week1[weekday] = wd1[count_z1]
            count_z1 += 1
        count_z2 = 0
        for weekday in weekdays:
            week2[weekday] = wd2[count_z2]
            count_z2 += 1

        return rozklad


# one_inst = Rozklad()
# x = one_inst.get_rozklad()

# conn = sqlite3.connect('rozklad.sqlite')
# cur = conn.cursor()
#
# cur.execute('''DROP TABLE IF EXISTS Classes''')
#
# cur.execute('''CREATE TABLE Classes
#     (id INTEGER UNIQUE, week_No INTEGER, weekday TEXT, No INTEGER, tm TEXT, teacher TEXT, class TEXT, room TEXT, link TEXT)''')
#
# print('Filling the Databse')
# count_id = 0
# for dayk, day in x['week1'].items():
#     w = 1
#     subj_count = 1
#     for subj in x['week1'][dayk]:
#         if subj != '':
#             print(subj)
#             cur.execute('''INSERT OR IGNORE INTO Classes (id, week_No, weekday, No, tm, teacher, class, room)
#                 VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )''', ( count_id, w, dayk, subj_count, subj[0], subj[1], subj[2], subj[3] ))
#             count_id += 1
#             print('Adding', subj)
#         subj_count += 1
#
#
# for dayk, day in x['week2'].items():
#     w = 2
#     subj_count = 1
#     for subj in x['week2'][dayk]:
#         if subj != '':
#             cur.execute('''INSERT OR IGNORE INTO Classes (id, week_No, weekday, No, tm, teacher, class, room)
#                 VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )''', ( count_id, w, dayk, subj_count, subj[0], subj[1], subj[2], subj[3] ))
#             count_id += 1
#             print('Adding', subj)
#         subj_count += 1
#
#
# conn.commit()
# conn.close()
# print('Database filled 50%')
# print('Might take a few minutes...')
