import requests
from fake_useragent import UserAgent
def readport():
    ip_list = []
    port_list = []
    with open("ipPort.txt","r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            ip_list.append(line.split(" ")[0])
            port_list.append(line.split(" ")[1])
    return ip_list,port_list

try:
    ua = UserAgent()
    url = "http://httpbin.org/get"
    header = {
        "User-Agent": ua.random
    }
    ip_list = []
    port_list = []
    ip_list,port_list = readport()
    for i in range(0, len(ip_list)):
        # print("使用代理ip:"+ip_list[i] + ":" + port_list[i])
        ip_port = ip_list[i] + ":" + port_list[i]
        proxy = {
            'http': ip_port
        }
        response = requests.get(url=url, headers=header, proxies=proxy, verify=False)
        page_text = response.text
        print(page_text)
except Exception:
    pass


