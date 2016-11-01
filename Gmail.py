# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
driver = webdriver.Chrome()
GMAIL_ADRESS = "frabro568@gmail.com"
GMAIL_PASS = "ndagmabry9"

def login(gmail_adress=GMAIL_ADRESS,gmail_pass=GMAIL_PASS):
    #page1
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/&hl=ja")
    elem = driver.find_element_by_css_selector('#Email')
    elem.send_keys(gmail_adress)
    elem = driver.find_element_by_css_selector('#next').click()
    sleep(0.5)
    elem = driver.find_element_by_css_selector('#Passwd')
    elem.send_keys(gmail_pass)
    sleep(0.5)
    elem = driver.find_element_by_css_selector('#signIn').click()

def getPinCode():
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/&hl=ja")
    sleep(5)
    elems = driver.find_elements_by_css_selector('span')
    for e in elems:
        if e.text == '40404':
            e.click()
            break
    elems = driver.find_elements_by_css_selector('div')
    sleep(3)
    pin_code = ""
    for e in elems:
        # print(e.text)
        pattern = r"Twitter認証コードは([0-9]*)です"
        repatter = re.compile(pattern)
        matchOB = repatter.findall(e.text)
        if len(matchOB) > 0:
            print("コード is:",matchOB[0])
            pin_code = matchOB[0]
    return pin_code
# driver.switch_to_window(driver.window_handles[-1])

if __name__ == '__main__':
    login()
    print(getPinCode())
