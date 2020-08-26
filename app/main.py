from flask import render_template, jsonify, request
from flask_cors import CORS, cross_origin
from app import app
from app.BLL import EmployeeSvc
from app.Common.EmployeeReq import EmployeeReq

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=['post'])
def test():
    return jsonify({'test': 1})



@app.route("/create-employee", methods=['post'])
def createEmployee():
    # Khi post theo file Json thì phải nhận request là get_json()

    data = request.get_json()
    #Tạo đối tượng
    req = EmployeeReq()
    #Đọc file JSON

    req.userName = data["userName"]
    req.password = data["password"]
    req.firstName = data["firstName"]
    req.lastName = data["lastName"]
    req.identityCard = data["identityCard"]
    req.phoneNumber = data["phoneNumber"]
    req.birthDay = data["birthDay"]
    req.gender = data["gender"]
    req.address = data["address"]
    req.note = data["note"]

    # import pdb
    # pdb.set_trace()

    return jsonify(EmployeeSvc.CreateEmpAccount(req)) #Xử lí lỗi trước khi return

if __name__ == "__main__":
    app.run(debug=True) #MỞ chế độ debug cho development