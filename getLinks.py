from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3
from time import sleep

class Google:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        self.driver=webdriver.Chrome('/Users/Max/Desktop/Code/Selenium/chromedriver')
        self.driver.get('https://www.coursera.org/?authMode=login')
        original_window = self.driver.current_window_handle
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="authentication-box-content"]/div/div[1]/div[1]/button/span').click()
        sleep(5)
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(Keys.RETURN)
        sleep(5)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(Keys.RETURN)
        sleep(5)
        self.driver.switch_to.window(original_window)


    def get_link(self, subject_url):
        self.driver.get(subject_url)
        sleep(5)
        the_link = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[2]/div[2]/span/a').get_attribute('href')

        # qu = input('Quit? y/n  ')
        # while True:
        #     if qu == 'y':
        #         self.driver.quit()
        #         break
        #     elif qu == 'n':
        #         sleep(10)
        return the_link

    def q(self):
        self.driver.quit()



username = 'cmi65436-ames22@lll.kpi.ua'
password = 'Killer0304'

# two_inst = Google(username, password)
# two_inst.login()
# toa = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg0Nzk1NDgw')
# moac = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyOTA5NzE0MzM2')
# two_inst.q()
# print(toa)
# print(moac)

link1 = '1'
link2 = '2'
links = [link1, ' ', link2]


conn = sqlite3.connect('rozklad.sqlite')
cur = conn.cursor()

print('Filling the Databse')
l_count = 1
for i in links:
    print('Adding', i)
    cur.execute("UPDATE Classes SET link = ? WHERE No = ?", (i, l_count))
    l_count += 1


conn.commit()
conn.close()
print('Database filled')
