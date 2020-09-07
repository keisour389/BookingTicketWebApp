from flask import render_template, jsonify, request, redirect
from flask_cors import CORS, cross_origin
from flask_login import login_user, current_user
from app import app, login
from app.models import * #import các model view vào sử dụng
import hashlib

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("home/home.html")


@app.route("/test", methods=['post'])
def test():
    return jsonify({'test': 1})

#Phải khai báo cú pháp này khi sử dụng login
@login.user_loader
def user_load(user_id):
    return Employee.query.get(user_id)

#features
@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        #Lấy từ form
        username = request.form.get("username")
        password = request.form.get("password")
        #Băm mật khẩu
        password = hashlib.md5(password.strip().encode("utf-8")).hexdigest()
        #Kiểm tra CSDL
        emp = Employee.query.filter(Employee.userName == username,
                                    Employee.password == password).first()
        import pdb
        pdb.set_trace()
        # emp = Employee.query.filter(Employee.userName == "1",
        #                             Employee.password == "1").first()
        if emp:
            login_user(user=emp) #Ghi nhận đã đăng nhập
    return redirect("/admin")

@app.route("/flight")
def flight():
    return render_template("flight/flight.html")

@app.route("/flight-list")
def flight_list():
    return render_template("flightlist/flightlist.html")

@app.route("/ticket")
def ticket():
    return render_template("ticket/ticket.html")

if __name__ == "__main__":
    app.run(debug=True) #MỞ chế độ debug cho development