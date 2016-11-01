# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
driver = webdriver.Chrome()
GMAIL_ADRESS = "frabro568@gmail.com"
GMAIL_PASS = "ndagmabry9"

driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/&hl=ja")

#page1
elem = driver.find_element_by_css_selector('#Email')
elem.send_keys(GMAIL_ADRESS)
elem = driver.find_element_by_css_selector('#next').click()
sleep(0.5)
elem = driver.find_element_by_css_selector('#Passwd')
elem.send_keys(GMAIL_PASS)
sleep(0.5)
elem = driver.find_element_by_css_selector('#signIn').click()
sleep(5)
elems = driver.find_elements_by_css_selector('span')
for e in elems:
    if e.text == '40404':
        e.click()
        break
elems = driver.find_elements_by_css_selector('div')
sleep(3)
for e in elems:
    # print(e.text)
    pattern = r"Twitter認証コードは([0-9]*)です"
    repatter = re.compile(pattern)
    matchOB = repatter.findall(e.text)
    if len(matchOB) > 0:
        print("コード is:",matchOB[0])
        break
# driver.switch_to_window(driver.window_handles[-1])
