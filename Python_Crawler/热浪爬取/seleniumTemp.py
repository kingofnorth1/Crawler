from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from loguru import logger

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("disable-blink-features=AutomationControlled")
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chromeOptions)
driver.get('https://hot.taobao.com/')
wait = WebDriverWait(driver, 50, 0.5)
time.sleep(3)


def login():
    logger.info(driver.current_url)
    if "https://hot.taobao" in driver.current_url:
        loginFirst = driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[1]/div[2]")
        logger.debug(loginFirst)
        if loginFirst is not None:
            loginFirst.click()
    time.sleep(3)
    code = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[3]/div/div/div/div[1]/i")))
    code.click()
    logger.info("等待结果")
    time.sleep(3)
    # code = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/i")))
    # code.click()
    userName = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/header/div[2]/div[2]/div/span[1]")))
    time.sleep(3)
    driver.get(
        "https://hot.taobao.com/hw/union/hw-alliance/store?checkIcTags=0&hasSample=0&isDirect=0&keyword=%E5%8F%A3%E7%BA%A2&lowPrice=30&rankType=2")
    time.sleep(3)
    userName = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/header/div[2]/div[2]/div/span[1]")))
    tbCookies = driver.get_cookies()
    cookie_dict = ""
    for item in tbCookies:
        cookie_dict += item['name']+"="+item['value']+"; "
    if not os.path.exists("cookiesPhone.txt"):
        with open('cookiesPhone.txt', "w") as f:
            f.write(str(cookie_dict))
    with open('cookiesPhone.txt', "a", encoding="utf-8") as f:
        f.write("\n"+str(cookie_dict))
    logger.debug(cookie_dict)
    return str(cookie_dict)

login()
driver.quit()
