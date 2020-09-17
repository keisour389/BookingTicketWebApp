from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)

# Secret key
app.secret_key = "b'\xfeu\xda]&\x07\xf9c\x93\x7f\xd0\xc7H\x1bzH'"  # secret_key dùng cho session
# Config với database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/bookingticketdb?charset=utf8mb4"  # charset cho unicode
# Thông báo khi có thay đổi

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# Tạo biến tương tác với CSDL
db = SQLAlchemy(app=app)
# Tạo trang admin
admin = Admin(app, "Quản lí bán vé may bay", template_mode="bootstrap3")
# Tạo trang đăng nhập
login = LoginManager(app=app)
