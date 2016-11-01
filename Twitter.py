from selenium import webdriver
from time import sleep

TWITTER_ID = "vitalinakudrya3"
TWITTER_PASS = "cmkUZyJytm"
TWITTER_EMAIL = ""

class Twitter:
    def __init__(self,twitter_id,twitter_pass,twitter_email):
        self.twitter_id = twitter_id
        self.twitter_pass = twitter_pass
        self.twitter_email = twitter_email
        self.driver = webdriver.Chrome()

        self.driver.get("https://twitter.com/login")
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
        elem.send_keys(self.twitter_id)
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
        elem.send_keys(self.twitter_pass)
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button')
        elem.click()
    def getDriver(self):
        return self.driver

    def setLangage(self):
        # page2
        self.driver.get('https://twitter.com/settings/account')
        if self.driver.title == "Twitter / 設定":
            return True
        elem = self.driver.find_element_by_css_selector('#user_lang')
        elem.find_element_by_css_selector("option[value='ja']").click()
        sleep(0.1)
        self.driver.find_element_by_css_selector('#settings_save').click()
        sleep(0.1)

        # page3
        elem = self.driver.find_element_by_css_selector('#auth_password')
        elem.send_keys(self.twitter_pass)
        elem = self.driver.find_element_by_css_selector('#save_password')
        elem.click()


    def setPhone(self,phone_number="0000"):
        self.driver.get('https://twitter.com/settings/add_phone')
        elem = self.driver.find_element_by_css_selector('#page-container > div.content-main > div.content-inner.no-stream-end > h3')
        if elem.text == "ご利用の携帯電話番号を確認してください。":
            return True
        elem = self.driver.find_element_by_css_selector('#device_country_code > option:nth-child(8)')
        elem.click()
        elem = self.driver.find_element_by_css_selector('#phone_number')
        elem.send_keys(phone_number)
        elem = self.driver.find_element_by_css_selector('#device_register')
        elem.click()


    def setPINKey(self,pin_code):
        self.driver.get('https://twitter.com/settings/add_phone')
        elem = self.driver.find_element_by_css_selector('#numeric_pin_raw')
        elem.send_keys(pin_code)
        elem = self.driver.find_element_by_css_selector('#device_verify')
        elem.click()
if __name__ == '__main__':
    tw = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL)
    tw.getDriver()
