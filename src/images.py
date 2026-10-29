# Bảng ảnh cho bản build: mỗi file trong assets/img/<key>.<ext> là một ảnh, khoá = tên file.
# Ảnh mới: chạy tools/add_image.py để nén WebP từ ảnh gốc (assets/source) rồi đặt vào assets/img.
# Nguồn gốc từng ảnh ghi ở specs/image-sources.json.
import os, base64
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'assets', 'img')
MIME = {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'png': 'image/png', 'webp': 'image/webp', 'svg': 'image/svg+xml'}

def image_table():
    T = {}
    for f in sorted(os.listdir(IMG)):
        k, ext = f.rsplit('.', 1)
        T[k] = 'data:%s;base64,%s' % (MIME[ext.lower()], base64.b64encode(open(os.path.join(IMG, f), 'rb').read()).decode())
    return T
