# ภารกิจที่ 3: Secret Knock & Drop (Socket & Port Knocking)
# สถานการณ์: เซิร์ฟเวอร์เป้าหมาย (10.10.10.99) ปิดพอร์ตทั้งหมดไว้ด้วย Firewall แต่แอดมินแอบซ่อนฟีเจอร์ "Port Knocking" เอาไว้ หากมีใครส่ง TCP Connection (แค่เชื่อมต่อแล้วปิด) ไปที่พอร์ต 1337, 7331, และ 8080 ตามลำดับ ภายในระยะเวลาไม่เกิน 2 วินาที Firewall จะยอมเปิดพอร์ต 9999 (ซึ่งเป็นช่องโหว่รอรับ Shell) ให้ชั่วคราว
# โจทย์:
# จงเขียนสคริปต์ Python ที่ใช้ไลบรารี socket ทำสิ่งต่อไปนี้:
# ทำ Port Knocking ตามลำดับ (1337 -> 7331 -> 8080) โดยมีดีเลย์เล็กน้อยระหว่างพอร์ต (เช่น 0.2 วินาที)
# เมื่อ Knock เสร็จ ให้พยายามเชื่อมต่อไปที่พอร์ต 9999 ทันที
# ถ้าเชื่อมต่อสำเร็จ ให้ส่ง Payload เป็นรหัส Base64 (สมมติว่าเป็นข้อความ base64_encoded_shell) ไปที่พอร์ตนั้น แล้วรอรับข้อความ "PWNED" ตอบกลับมา



import time
import socket
import base64

ip = "10.10.10.99"
ports = ['1337','7331','8080']

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(0.2)
# s.connect(ip,1337)
# s.close()
# time.sleep(0.2)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(0.2)
# s.connect(ip,7331)
# s.close()
# time.sleep(0.2)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(0.2)
# s.connect(ip,8080)
# s.close()
# time.sleep(0.2)


for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect(ip,port)
        s.close()
        time.sleep(0.2) #delay ระหว่าง port
    except Exception as e:
        print(f"[-] failed to connect port {port}")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    s.connect(ip,9999)

    payload = "base64_encoded_shell"

    payload_encode = base64.b64encode(payload.encode("utf-8")) #s.send() รับข้อมูลที่เป็น byte เท่านั้น เลยไม่ต้อง encode
    s.send(payload_encode +b'\r\n')
    response = s.recv(1024)
except Exception as e:
    print("[-] failed to connect port 9999")

if response.decode('utf-8').strip() =='PWNED' :
    print("[!!!] Successfully connected, welcome!")
else:
    print("[-] failed to connect.")






