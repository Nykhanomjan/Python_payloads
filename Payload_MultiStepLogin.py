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