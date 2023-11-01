# list_s = []
# if (len(list_s) == 0):
#     print("sb")
global cookie_num
cookie_num = 0
def readCookie():
    cookie = ""
    global cookie_num
    with open("cookies.txt", "r") as f:
        cookie_list = f.readlines();
        if (cookie_num<=len(cookie_list)-1):
            for i in range(0, len(cookie_list)):
                if (i == cookie_num):
                    cookie_list[i] = cookie_list[i].strip("\n")
                    cookie = cookie_list[i]
        else:
            input("cookie已经消耗完毕！！！")
            quit()
    cookie_num += 1
    return cookie


print(type(readCookie()))
print("1fsdf:    "+readCookie())
print("1fsdf:    "+readCookie())
print("1fsdf:    "+readCookie())
print("1fsdf:    "+readCookie())
print("1fsdf:    "+readCookie())
print("1fsdf:    "+readCookie())
print("1fsdf:    "+readCookie())

