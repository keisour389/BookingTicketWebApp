from flask import render_template, jsonify, request, url_for, session, redirect
from flask_login import login_user, current_user
from app import app, login, dao
from app.models import *  # import các model view vào sử dụng
from app.decorator import login_required
import hashlib



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/navbar")
def navbar():
    return render_template("navbar/navbar.html")


@app.route("/test", methods=['post'])
def test():
    return jsonify({'test': 1})


# Phải khai báo cú pháp này khi sử dụng login
@login.user_loader
def user_load(user_id):
    return Employee.query.get(user_id)


# features
@app.route("/login-admin", methods=["get", "post"])
def login_admin():
    if request.method == "POST":
        # Lấy từ form
        username = request.form.get("username")
        password = request.form.get("password")
        # Băm mật khẩu
        password = hashlib.md5(password.strip().encode("utf-8")).hexdigest()
        # Kiểm tra CSDL
        emp = dao.validate_user(username=username, password=password)
        # import pdb
        # pdb.set_trace()
        # emp = Employee.query.filter(Employee.userName == "1",
        #                             Employee.password == "1").first()
        if emp:
            login_user(user=emp)  # Ghi nhận đã đăng nhập
    return redirect("/admin")


@app.route("/flight")
@login_required
def flight():
    airport = Airport.query.all()  # Lấy cả sân bay
    return render_template("flight/flight.html", airport=airport)


@app.route("/login", methods=["get", "post"])
def login():
    err_msg = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cus = dao.validate_user(username=username, password=password)
        if cus:
            session["cus"] = username
            if "next" in request.args:
                return redirect(url_for(request.args["next"]))
            return redirect(url_for("index"))
        else:
            err_msg = "ĐĂNG NHẬP KHÔNG THÀNH CÔNG"
    return render_template("login/login.html", err_msg=err_msg)


@app.route("/logout")
def logout():
    session["cus"] = None
    return redirect(url_for("index"))


@app.route("/search-flight")
def search_flight():
    # Lấy các giá trị từ query param
    start = request.args.get('start')
    end = request.args.get('end')

    # startID = search_airport_id_by_name(start)
    # endID = search_airport_id_by_name(end)

    # Lọc
    flightList = FlightSchedules.query \
        .filter(FlightSchedules.airportToTakeOff == start, FlightSchedules.airportToLanding == end) \
        .all()
    # flightList = Airport.query.join(FlightSchedules, Airport.airportID == FlightSchedules.airportToTakeOff)\
    #     .add_columns(Airport.airportID, Airport.name, FlightSchedules.flightSchedulesID, FlightSchedules.flightDateTime)\
    #     .filter(Airport.airportID == start)
    # flightListString = ''.join(map(str, flightList))
    # import pdb
    # pdb.set_trace()
    # test = ""
    # for flight in flightList:
    #     test += flight.name + " "

    # return jsonify({'start': start, 'end': end, 'data': test})
    return render_template('flightlist/flightlist.html', flightList=flightList)  # Transfer data


def search_airport_id_by_name(name):
    result = Airport.query.filter(Airport.airportID == name).first()
    return result


@app.route("/flight-list")
def flight_list():
    return render_template("flightlist/flightlist.html")


@app.route("/ticket")
def ticket():
    return render_template("ticket/ticket.html")


@app.route("/register", methods=["post", "get"])
def register():
    err_msg = ""
    if request.method == "POST":
        userName = request.form.get("userName")
        password = request.form.get("password")
        lastName = request.form.get("lastName")
        firstName = request.form.get("firstName")
        identityCard = request.form.get("identityCard")
        phoneNumber = request.form.get("phoneNumber")
        birthDay = request.form.get("birthDay")
        gender = request.form.get("gender")
        address = request.form.get("address")
        note = request.form.get("note")
        cus = dao.create_cus(userName=userName, password=password, lastName=lastName, firstName=firstName,
                             identityCard=identityCard, phoneNumber=phoneNumber, birthDay=birthDay, gender=gender,
                             address=address, note=note)
        if cus:
            return redirect(url_for("index"))
        else:
            err_msg = "ĐĂNG KÍ KHÔNG THÀNH CÔNG"
    return render_template("register/register.html", err_msg=err_msg)


@app.route("/create-ticket", methods=["POST"])
@login_required
def create_ticket():
    # Lấy file JSON từ JS
    data = request.get_json()
    # Đọc file JSON
    identityCard = data["identityCard"]
    phoneNumber = data["phoneNumber"]
    ticketClass = data["ticketClass"]
    price = data["price"]
    note = data["note"]
    employeeID = data["employeeID"]
    customerID = data["customerID"]
    flightSchedulesID = data["flightSchedulesID"]
    # import pdb
    # pdb.set_trace()
    result = dao.create_ticker(identityCard=identityCard, phoneNumber=phoneNumber, ticketClass=ticketClass,
                               price=price, note=note, employeeID=employeeID, customerID=customerID,
                               flightSchedulesID=flightSchedulesID)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)  # MỞ chế độ debug cho development
