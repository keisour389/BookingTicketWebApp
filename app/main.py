from flask import render_template, jsonify, request, redirect
from flask_cors import CORS, cross_origin
from flask_login import login_user, current_user
from app import app, login, dao
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
        # import pdb
        # pdb.set_trace()
        # emp = Employee.query.filter(Employee.userName == "1",
        #                             Employee.password == "1").first()
        if emp:
            login_user(user=emp) #Ghi nhận đã đăng nhập
    return redirect("/admin")

@app.route("/flight")
def flight():
    airport = Airport.query.all() #Lấy cả sân bay
    return render_template("flight/flight.html", airport=airport)

@app.route("/search-flight")
def search_flight():
    #Lấy các giá trị từ query param
    start = request.args.get('start')
    end = request.args.get('end')

    # startID = search_airport_id_by_name(start)
    # endID = search_airport_id_by_name(end)

    #Lọc
    flightList = FlightSchedules.query\
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
    return render_template('flightlist/flightlist.html', flightList=flightList) #Transfer data

def search_airport_id_by_name(name):
    result = Airport.query.filter(Airport.airportID == name).first()
    return result

@app.route("/flight-list")
def flight_list():
    return render_template("flightlist/flightlist.html")

@app.route("/ticket")
def ticket():
    return render_template("ticket/ticket.html")

@app.route("/create-ticket", methods=["POST"])
def create_ticket():
    #Lấy file JSON từ JS
    data = request.get_json()
    #Đọc file JSON
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
    result = dao.create_ticker(identityCard=identityCard,phoneNumber=phoneNumber, ticketClass=ticketClass,
                             price=price, note=note, employeeID=employeeID, customerID=customerID,
                            flightSchedulesID=flightSchedulesID)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True) #MỞ chế độ debug cho development