import requests
from fake_useragent import UserAgent

ua = UserAgent()
url = "http://httpbin.org/get"
header = {
    "User-Agent": ua.random
}
# proxy = {
#     'http': "222.74.73.202:42055"
# }
# response = requests.get(url=url, headers=header, proxies=proxy, verify=False)
response = requests.get(url=url, headers=header)
if response.status_code == requests.codes.ok:
	# print('Request Successfully')
    print(type(response.status_code))
else:
	exit()
# print(page_text)