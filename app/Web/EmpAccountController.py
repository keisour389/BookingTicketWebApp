from flask import Flask, render_template, jsonify, request, session
from flask_cors import CORS, cross_origin
from app import app
from app.BLL import EmployeeSvc
from app.Common.EmployeeReq import EmployeeReq

app.secret_key = b's\xb2\xf1\xe5\x15\x92\xb8\xbc/_M\xc5w\xb9}\x0b'
cors = CORS(app)

@app.route("/")
def index(self):
    return render_template("index.html")

@app.route("/create-employee", methods = ['POST'])
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


    return jsonify(EmployeeSvc.createEmpAccount(req))

@app.route("/validate-user", methods = ['POST'])
def validateUser():
    # Khi post theo file Json thì phải nhận request là get_json()
    data = request.get_json()
    userName: str = data["userName"]
    password: str = data["password"]
    res = EmployeeSvc.validateUser(userName, password)
    if res["success"]:
        session['userName'] = userName
        import pdb
        pdb.set_trace()
    return res

@app.route("/logged", methods = ['GET'])
def logged():
    # result: str = ""
    # import pdb
    # pdb.set_trace()
    # try:
    #     result = session["userName"]
    # except:
    #     return {
    #         "userName": "",
    #         "logged": False
    #     }
    #Lấy được session
    import pdb
    pdb.set_trace()
    if 'username' in session:
        return {
            "userName": session['userName'],
            "logged": True
        }
    return {
        "userName": "",
        "logged": False
    }


if __name__ == "__main__":
    app.run(debug=True) #MỞ chế độ debug cho development