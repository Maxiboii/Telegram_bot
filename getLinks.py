#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3
from time import sleep


class Google:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        try:
            self.driver=webdriver.Chrome('/Users/Max/Desktop/Code/Selenium/chromedriver')
        except:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Chrome('/home/maksimchichkan90/Downloads/chromedriver', chrome_options=chrome_options)
        self.driver.get('https://www.coursera.org/?authMode=login')
        original_window = self.driver.current_window_handle
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="authentication-box-content"]/div/div[1]/div[1]/button/span').click()
        sleep(5)
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.switch_to.window(original_window)


    def get_link(self, subject_url):
        self.driver.get(subject_url)
        sleep(5)
        the_link = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[2]/div[2]/span/a').get_attribute('href')

        return the_link

    def q(self):
        self.driver.quit()



# two_inst = Google(username, password)
# two_inst.login()
# sleep(20)
# two_inst.q()
