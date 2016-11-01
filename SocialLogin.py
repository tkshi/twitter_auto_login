# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
from Twitter import Twitter
OAUTH_SITE_URL = "http://36.55.241.31/twitter/admin/Share/login"
LOGIN_URL = "http://36.55.241.31/twitter/admin"
LOGIN_ID = "admin"
LOGIN_PASS = "1234567"

TWITTER_ID = "vitalinakudrya3"
TWITTER_PASS = "cmkUZyJytm"
TWITTER_EMAIL = ""


class SocialLogin:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(LOGIN_URL)
        elem = self.driver.find_element_by_css_selector('#AdminUsername')
        elem.send_keys(LOGIN_ID)
        elem = self.driver.find_element_by_css_selector('#AdminPassword')
        elem.send_keys(LOGIN_PASS)
        elem = self.driver.find_element_by_css_selector('#AdminAdminIndexForm > fieldset > input.btn.btn-lg.btn-success.btn-block')
        elem.click()

    def twitterLogin(self):
        self.driver.get(OAUTH_SITE_URL)
        elem = self.driver.find_element_by_css_selector('#allow')
        elem.click()


if __name__ == '__main__':
    driver = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL).getDriver()
    sl = SocialLogin(driver=driver)
    sl.twitterLogin()
