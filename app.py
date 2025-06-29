from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # ใช้สำหรับ flash message

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# สร้างโฟลเดอร์ uploads ถ้ายังไม่มี
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# หน้าแรก แสดงรายชื่อไฟล์
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

# อัปโหลดหลายไฟล์
@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        flash('ไม่มีไฟล์ที่เลือก')
        return redirect(url_for('index'))

    files = request.files.getlist('file')  # ⬅️ รองรับหลายไฟล์
    count = 0

    for file in files:
        if file and file.filename:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            count += 1

    flash(f'อัปโหลดสำเร็จ {count} ไฟล์')
    return redirect(url_for('index'))

# ดาวน์โหลดไฟล์
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# ลบไฟล์
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash(f'ลบไฟล์ {filename} แล้ว')
    else:
        flash('ไม่พบไฟล์')
    return redirect(url_for('index'))

# รันแอป
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
