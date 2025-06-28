# เว็บเซิร์ฟเวอร์อัปโหลดและดาวน์โหลดไฟล์ด้วย Flask

เว็บแอปพลิเคชันที่เขียนด้วย Python Flask สำหรับ:

- อัปโหลดไฟล์ผ่านเว็บเบราว์เซอร์
- แสดงรายชื่อไฟล์ที่อัปโหลด
- ดาวน์โหลดไฟล์ที่อัปโหลด

## ✅ คุณสมบัติ

- รองรับการอัปโหลดไฟล์ทุกประเภท
- บันทึกไฟล์ไว้ในโฟลเดอร์ `uploads/`
- คลิกเพื่อดาวน์โหลดไฟล์ที่อัปโหลดแล้ว

## 📦 สิ่งที่ต้องมี

- Python 3.7 ขึ้นไป
- Flask

## 🔧 วิธีติดตั้ง

```bash
# โคลนโปรเจกต์จาก GitHub
git clone https://github.com/karndiy/pywebupload.git
cd pywebupload

# (แนะนำ) สร้าง virtual environment
python -m venv venv
venv\Scripts\activate  # สำหรับ Windows
source venv/bin/activate  # สำหรับ Linux/Mac

# ติดตั้ง Flask
pip install flask
