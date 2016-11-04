# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from Error import *

TWITTER_ID = "domnikasamsono4"
TWITTER_PASS = "fDuJ4GD8A6"
TWITTER_EMAIL = "domnika-samsonova@mail.ru"


# TWITTER_ID = "denisovafloren9"
# TWITTER_PASS = "sJjwfQwRa6"
# TWITTER_EMAIL = "DenisovaFlorensa1983@mail.ru"

class Twitter:
    def __init__(self,twitter_id,twitter_pass,twitter_email):
        self.twitter_id = twitter_id
        self.twitter_pass = twitter_pass
        self.twitter_email = twitter_email
        self.driver = webdriver.Chrome()
        self.success_login = False

        self.driver.get("https://twitter.com/login")
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
        elem.send_keys(self.twitter_id)
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
        elem.send_keys(self.twitter_pass)
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button')
        elem.click()

        try:
            elem = self.driver.find_element_by_css_selector('#challenge_response')
            elem.send_keys(self.twitter_email)
            elem = self.driver.find_element_by_css_selector('#email_challenge_submit')
            elem.click()
        except NoSuchElementException as e:
            print('none')
        try:
            elem = self.driver.find_element_by_css_selector('#tweet-box-home-timeline')
            self.success_login = True
        except Exception:
            self.driver.close()
            raise TwitterLoginError()
            self.success_login = False


    def getLoginStatus(self):
        return self.success_login

    def getDriver(self):
        return self.driver

    def setLangage(self):
        # page2
        self.driver.get('https://twitter.com/settings/account')
        if self.driver.title == u"Twitter / 設定":
            return True
        elem = self.driver.find_element_by_css_selector('#user_lang')
        elem.find_element_by_css_selector("option[value='ja']").click()
        sleep(1)
        self.driver.find_element_by_css_selector('#settings_save').click()
        sleep(1)

        # page3
        elem = self.driver.find_element_by_css_selector('#auth_password')
        elem.send_keys(self.twitter_pass)
        elem = self.driver.find_element_by_css_selector('#save_password')
        elem.click()


    def setPhone(self,phone_number="0000"):
        self.driver.get('https://twitter.com/settings/add_phone')
        elem = self.driver.find_element_by_css_selector('#page-container > div.content-main > div.content-inner.no-stream-end > h3')
        elem = self.driver.find_element_by_css_selector('#device_country_code > option:nth-child(8)')
        elem.click()
        elem = self.driver.find_element_by_css_selector('#phone_number')
        elem.send_keys(phone_number)
        elem = self.driver.find_element_by_css_selector('#device_register')
        elem.click()
        try:
            elem = self.driver.find_element_by_css_selector('#settings-alert-box > h4')
            sleep(0.5)
            if elem.text == u"この操作は許可されていません":
                return False
        except Exception:
            print('except')
        return True
    def close(self):
        self.driver.close()

    def setPINKey(self,pin_code):
        self.driver.get('https://twitter.com/settings/add_phone')
        elem = self.driver.find_element_by_css_selector('#numeric_pin_raw')
        elem.send_keys(pin_code)
        elem = self.driver.find_element_by_css_selector('#device_verify')
        elem.click()
if __name__ == '__main__':
    tw = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL)
    print(tw.getLoginStatus())
    tw.setLangage()
    print(tw.setPhone(phone_number="(843) 471-0879"))
