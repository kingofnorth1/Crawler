from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("disable-blink-features=AutomationControlled")
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chromeOptions)

driver.get('https://www.baidu.com')
# wait = WebDriverWait(driver, 10, 0.5)
# # 等待滑块按钮加载
# div = wait.until(EC.presence_of_element_located((
#     By.ID, 'nc_1__bg'
# )))
# # 休眠2s，等待滑块按钮加载
# time.sleep(3)
# # 点击并按住滑块
# ActionChains(driver).click_and_hold(div).perform()
# # 移动滑块
# ActionChains(driver).move_by_offset(xoffset=300, yoffset=0).perform()
# # 等待验证通过
# wait.until(EC.text_to_be_present_in_element((
#     By.CSS_SELECTOR, 'div#nc_1__scale_text > span.nc-lang-cnt > b'), '验证通过'
# ))
# login = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_enterBtn_8ebnb_1")))
# login.click()
# code = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[3]/div/div/div/div[1]/i")))
# code.click()
#
time.sleep(100)
driver.quit()
