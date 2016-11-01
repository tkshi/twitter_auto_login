from Gmail import *
from SocialLogin import *
from Twitter import *


TWITTER_ID = "vitalinakudrya3"
TWITTER_PASS = "cmkUZyJytm"
TWITTER_EMAIL = ""

GMAIL_ADRESS = "frabro568@gmail.com"
GMAIL_PASS = "ndagmabry9"
PHONE_NUMBER = "(830) 308-7334"

tw = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL)
# tw.setLangage()
# tw.setPhone(phone_number=PHONE_NUMBER)
# gm = Gmail(gmail_adress=GMAIL_ADRESS,gmail_pass=GMAIL_PASS)
# pin_code = gm.getPinCode()
# sleep(5)
# tw.setPINKey(pin_code=pin_code)

driver = tw.getDriver()
sl = SocialLogin(driver=driver)
sl.twitterLogin()
driver.close()
