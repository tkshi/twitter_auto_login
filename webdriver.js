var randomstring = require("randomstring");
require('chromedriver')

const full_name = randomstring.generate();

const password = randomstring.generate();
const SELENIUM_HOST = process.env.SELENIUM_HOST
const INET_ID = process.env.INET_ID || "PXUAR1R6"
const PASSWORD = process.env.PASSWORD || "7DujNJVk"

var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;



export default function(){
  if(SELENIUM_HOST){
    var driver = new webdriver.Builder()
        .forBrowser('chrome')
        .usingServer(`http://${SELENIUM_HOST}:4444/wd/hub`)
        .build();
  }else{
    var driver = new webdriver.Builder()
        .forBrowser('chrome')
        .build();
  }
  driver.get('http://www.jra.go.jp/IPAT_TAIKEN/s-pat/pw_010_i.html');
  driver.findElement(By.css('#top > div.bg-block > div > table > tbody > tr > td:nth-child(2) > div > div > form > table.input > tbody > tr > td:nth-child(2) > span > input[type="text"]')).sendKeys(INET_ID);
  driver.findElement(By.css('#top > div.bg-block > div > table > tbody > tr > td:nth-child(2) > div > div > form > table.input > tbody > tr > td:nth-child(3) > p > a')).click();
  console.log(driver)
  let newWindow = driver.getAllWindowHandles()
  driver.switchTo().window(newWindow);
  // driver.get('https://twitter.com/search?f=users&vertical=default&q=%E3%83%86%E3%82%B9%E3%83%88&src=typd');
  // let followButtons = driver.findElements(By.css('span.button-text.follow-text'));
  // console.log(driver.findElement(By.css('span.button-text.follow-text')))
  // followButtons.then(function (elements) {
  //   var pendingHtml = elements.map((folloButton)=>{
  //     folloButton.click()
  //   })
  //   webdriver.promise.all(pendingHtml).then(function (allHtml) {
  //     console.log("")
  //   });
  // });
  driver.takeScreenshot().then(
  function(image, err) {
      require('fs').writeFile('out.png', image, 'base64', function(err) {
          console.log(err);
          // driver.quit();
      });
  }
  );

}
