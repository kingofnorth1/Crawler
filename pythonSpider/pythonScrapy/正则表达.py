import requests
import re

temp = "fdsjlkfjsdlkjgoliAkrsngds3441423164@qq.comjfdsiklhjfgdlskjflidsjdflskjflksd;jf"
rule = r"[A-Za-z0-9\._+]{10}@[A-Za-z]+\.(com|edu|org|net)"
print(re.search(rule, temp))