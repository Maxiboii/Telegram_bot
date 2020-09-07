from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
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

    def get_tomorrow(self):

        url = 'http://rozklad.kpi.ua/Schedules/ViewSchedule.aspx?g=89a385d9-a264-4981-aa91-d7e12eb14730'
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")

        w1 = soup('table')[0]
        w2 = soup('table')[1]
        week1 = {}
        tuesday = {}
        week1['tuesday'] = tuesday
        tuesday[1] = w2.tr.next_sibling.td.next_sibling.next_sibling.text
        tuesday[2] = w2.tr.next_sibling.next_sibling.td.next_sibling.next_sibling.text
        tuesday[3] = w2.tr.next_sibling.next_sibling.next_sibling.td.next_sibling.next_sibling.text
        return week1['tuesday']





# one_inst = Rozklad()
# print(one_inst.get_tomorrow())
