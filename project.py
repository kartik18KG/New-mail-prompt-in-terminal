from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("/Users/kartikgupta/Downloads/chromedriver")

username = "enter your username"
password = "enter your password"
url = "https://www.gmail.com"
import datetime


driver.get(url)
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(
    password
)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(
    Keys.ENTER
)
time.sleep(10)
i = 1
while i < 5:
    driver.find_element_by_xpath(
        '//*[@id=":4"]/div/div[1]/div[1]/div/div/div[5]/div/div'
    ).click()
    mail1 = driver.find_element_by_xpath('//*[@class="zA zE"]').get_attribute("id")
    time.sleep(10)
    mail2 = driver.find_element_by_xpath('//*[@class="zA zE"]').get_attribute("id")
    if mail1 == mail2:
        continue
    else:
        current_time = datetime.datetime.now()
        print("New mail : {}".format(current_time))
        continue
