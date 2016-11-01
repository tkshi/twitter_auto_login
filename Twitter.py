from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

TWITTER_ID = "vitalinakudrya3"
TWITTER_PASS = "cmkUZyJytm"
TWITTER_EMAIL = ""

def login():
    #page1
    driver.get("https://twitter.com/login")
    elem = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
    elem.send_keys(TWITTER_ID)
    elem = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
    elem.send_keys(TWITTER_PASS)
    elem = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button')
    elem.click()
    return driver

def setLangage():
    # page2
    driver.get('https://twitter.com/settings/account')
    elem = driver.find_element_by_css_selector('#user_lang')
    elem.find_element_by_css_selector("option[value='ja']").click()
    sleep(0.1)
    driver.find_element_by_css_selector('#settings_save').click()
    sleep(0.1)

    # page3
    elem = driver.find_element_by_css_selector('#auth_password')
    elem.send_keys(TWITTER_PASS)
    elem = driver.find_element_by_css_selector('#save_password')
    elem.click()


def setPhone(phone_number="0000"):
    driver.get('https://twitter.com/settings/add_phone')
    elem = driver.find_element_by_css_selector('#device_country_code > option:nth-child(8)')
    elem.click()
    elem = driver.find_element_by_css_selector('#phone_number')
    elem.send_keys(phone_number)
    elem = driver.find_element_by_css_selector('#device_register')
    elem.click()


def setPINKey(pin_code):
    driver.get('https://twitter.com/settings/add_phone')
    elem = driver.find_element_by_css_selector('#numeric_pin_raw')
    elem.send_keys(pin_code)
    elem = driver.find_element_by_css_selector('#device_verify')
    elem.click()
if __name__ == '__main__':
    login()
    # setLangage()
    # setPhone()
    setPINKey('440000')
