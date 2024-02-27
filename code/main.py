from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()

userid = os.environ['id']
userpass = os.environ['pass']
text = os.environ['text']
# driverの場所
# service = Service(executable_path="")
# driver = webdriver.chrome(service=service)
# driver.get("")
# time.sleep(10)

url = os.environ['url']
options = webdriver.ChromeOptions()
#　ログ出力を無くす
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Remote(
  command_executor = 'http://selenium:4444/wd/hub',
  options = options
)
driver.implicitly_wait(10)
driver.get(url)
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID,  "submit"))
)
input_id_elemnt = driver.find_element(By.ID, "userId")
input_id_elemnt.send_keys(userid)
input_pass_elemnt = driver.find_element(By.ID, "password")
input_pass_elemnt.send_keys(userpass + Keys.ENTER)
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID,  "globalSearch"))
)
input_id_elemnt = driver.find_element(By.ID, "globalSearch")
input_id_elemnt.send_keys(text + Keys.ENTER)
WebDriverWait(driver, 15).until(
  EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text))
)
## 部分一致
link = driver.find_element(By.PARTIAL_LINK_TEXT, text)
link.click()
WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.LINK_TEXT, "Wiki"))
)
## 完全一致
link = driver.find_element(By.LINK_TEXT, "Wiki")
link.click()
time.sleep(5)
driver.quit()
