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
        mon = [x.td.next_sibling.text for x in mon]

        tue = [x for x in w1.tr.next_siblings]
        tue.remove(tue[-1])
        tue = [x.td.next_sibling.next_sibling.text for x in tue]

        wed = [x for x in w1.tr.next_siblings]
        wed.remove(wed[-1])
        wed = [x.td.next_sibling.next_sibling.next_sibling.text for x in wed]

        thu = [x for x in w1.tr.next_siblings]
        thu.remove(thu[-1])
        thu = [x.td.next_sibling.next_sibling.next_sibling.next_sibling.text for x in thu]

        fri = [x for x in w1.tr.next_siblings]
        fri.remove(fri[-1])
        fri = [x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text for x in fri]

        sat = [x for x in w1.tr.next_siblings]
        sat.remove(sat[-1])
        sat = [x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text for x in sat]
        wd1 = [mon, tue, wed, thu, fri, sat]

        mon = [x for x in w2.tr.next_siblings]
        mon.remove(mon[-1])
        mon = [x.td.next_sibling.text for x in mon]

        tue = [x for x in w2.tr.next_siblings]
        tue.remove(tue[-1])
        tue = [x.td.next_sibling.next_sibling.text for x in tue]

        wed = [x for x in w2.tr.next_siblings]
        wed.remove(wed[-1])
        wed = [x.td.next_sibling.next_sibling.next_sibling.text for x in wed]

        thu = [x for x in w2.tr.next_siblings]
        thu.remove(thu[-1])
        thu = [x.td.next_sibling.next_sibling.next_sibling.next_sibling.text for x in thu]

        fri = [x for x in w2.tr.next_siblings]
        fri.remove(fri[-1])
        fri = [x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text for x in fri]

        sat = [x for x in w2.tr.next_siblings]
        sat.remove(sat[-1])
        sat = [x.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text for x in sat]
        wd2 = [mon, tue, wed, thu, fri, sat]

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
