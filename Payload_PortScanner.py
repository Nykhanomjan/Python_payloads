# ภารกิจที่ 4: "สร้างเรดาร์สแกนประตูหลังแบบติดเทอร์โบ" (หมวด Socket & Threading)

# สถานการณ์:
# คุณต้องการตรวจสอบว่าเครื่องเป้าหมาย (IP: 127.0.0.1) มีพอร์ตแปลกๆ เปิดทิ้งไว้บ้างหรือไม่ หากสแกนทีละพอร์ตตั้งแต่ 1 ถึง 1024 ด้วยโค้ดแบบปกติจะใช้เวลานานมาก

# โจทย์ที่คุณต้องเขียนโค้ด:
# จงเขียนสคริปต์ Port Scanner ด้วยไลบรารี socket เพื่อสแกนพอร์ตตั้งแต่ 1 ถึง 1024 โดยข้อบังคับคือ ต้องใช้ไลบรารี threading เพื่อให้รันการสแกนหลายๆ พอร์ตพร้อมกัน (Multithreading) และถ้าเจอพอร์ตไหนเปิด (เชื่อมต่อสำเร็จ คืนค่า 0) ให้พิมพ์บอกว่า "Port [พอร์ต] is OPEN"

# 💡 คำใบ้ (Hint):
# สร้างฟังก์ชัน scan_port(port) แยกต่างหาก
# ในลูปสแกน ให้สร้าง Thread ใหม่ threading.Thread(target=scan_port, args=(port,))
# เพื่อให้สคริปต์ไม่ค้างนาน ควรตั้ง socket.setdefaulttimeout(0.5) (รอแค่ครึ่งวินาทีพอ)


import socket
import concurrent.futures

ip = "127.0.0.1"

# คู่มือลูกน้อง (คงไว้เหมือนเดิมเป๊ะ)
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

try:
    print("[*] เริ่มต้นการสแกนด้วย Thread Pool (จำกัด 50 Threads)...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        
        # 3. โยนงานทั้งหมด (range 1-1025) ลงไปให้ฟังก์ชัน scan_port ช่วยกันทำ
        # คำสั่ง .map จะจัดการกระจายงานและวนลูปให้เราเองโดยอัตโนมัติ!
        executor.map(scan_port, range(1, 1025))

    print("[*] สแกนเสร็จสิ้นทั้งหมด!")

except Exception as e:
    print(f"Error: {e}")