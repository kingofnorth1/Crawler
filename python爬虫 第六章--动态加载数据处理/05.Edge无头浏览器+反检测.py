from selenium import webdriver
from time import sleep
#实现无可视化界面
from selenium.webdriver.edge.options import Options
#实现规避检测
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

#实现无可视化界面的操作
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "",
    "platform": "WINDOWS",
    # 关键是下面这个
    "ms:edgeOptions": {
        'extensions': [],
        'args': [
            '--headless',
            '--disable-gpu',
            '--remote-debugging-port=9222',
        ]}
}

#实现规避检测
option = EdgeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

#如何实现让selenium规避被检测的风险
bro = webdriver.Edge(executable_path='./msedgedriver.exe',capabilities=EDGE)

#无可视化界面(无头浏览器)   phantomjs
bro.get('https://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()