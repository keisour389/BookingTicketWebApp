from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.secret_key="123"



#Config với database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Truyen123@localhost/bookingticket?charset=utf8mb4" #charset cho unicode
#Thông báo khi có thay đổi
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#Tạo biến tương tác với CSDL
db = SQLAlchemy(app=app)


admin = Admin(app=app, name="QUAN LY BAN VE", template_mode="bootstrap3")
login = LoginManager(app=app)
Bootstrap(app=app)