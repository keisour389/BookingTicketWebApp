from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)




#Config với database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Banaccroi123@localhost/bookingticketdb?charset=utf8mb4" #charset cho unicode
#Thông báo khi có thay đổi
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#Tạo biến tương tác với CSDL
db = SQLAlchemy(app=app)