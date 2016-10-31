from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()

driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/&hl=ja")

#page1
elem = driver.find_element_by_css_selector('#Email')
elem.send_keys("godfri30@gmail.com")
elem = driver.find_element_by_css_selector('#next').click()
sleep(0.5)
elem = driver.find_element_by_css_selector('#Passwd')
elem.send_keys("idsnave9da")
sleep(0.5)
elem = driver.find_element_by_css_selector('#signIn').click()

# driver.switch_to_window(driver.window_handles[-1])

# page2
elem = driver.find_element_by_css_selector('#top > div.bg-block > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span > input[type="text"]')
elem.send_keys("62837393")
sleep(0.5)

elem = driver.find_element_by_css_selector('#top > div.bg-block > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span > input[type="password"]')
elem.send_keys("1920")
sleep(0.5)

elem = driver.find_element_by_css_selector('#top > div.bg-block > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > span > input[type="text"]')
elem.send_keys("3006")
sleep(0.5)

elem = driver.find_element_by_css_selector('#top > div.bg-block > div > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > p > a')
elem.click()

# page3
elem = driver.find_element_by_css_selector('#top > div.bg-block > div > form > p > input[type="submit"]')
elem.click()

# page4
elem = driver.find_element_by_css_selector('#b_area > div:nth-child(3) > ul > li:nth-child(1) > a')
elem.click()

# page5
elem = driver.find_element_by_css_selector('#gi_area > div > table > tfoot > tr > td > table > tbody > tr:nth-child(2) > td.auto > p.button > input[type="submit"]')
elem.click()

# page6
elem = driver.find_element_by_css_selector('#vi_area > div > div.appli > p:nth-child(1) > input[type="text"]')
elem.send_keys("12")
sleep(0.5)

elem = driver.find_element_by_css_selector('#vi_area > div > div.appli > p:nth-child(2) > input[type="text"]')
elem.send_keys("10")
sleep(0.5)

elem = driver.find_element_by_css_selector('#vi_area > div > div.editbtn > span > input[type="button"]')
elem.click()

# page6
elem = driver.find_element_by_css_selector('#i_area > table > tbody > tr:nth-child(1) > td > input[type="text"]')
elem.clear()
elem.send_keys("62837393")
sleep(0.5)

elem = driver.find_element_by_css_selector('#i_area > table > tbody > tr:nth-child(2) > td > input[type="password"]')
elem.send_keys("1920")
sleep(0.5)

elem = driver.find_element_by_css_selector('#i_area > table > tbody > tr:nth-child(3) > td > input[type="text"]')
elem.clear()
elem.send_keys("3006")
sleep(0.5)

elem = driver.find_element_by_css_selector('#i_area > table > tbody > tr:nth-child(4) > td > input[type="text"]:nth-child(1)')
elem.send_keys("12000")
sleep(0.5)
# driver.close()
