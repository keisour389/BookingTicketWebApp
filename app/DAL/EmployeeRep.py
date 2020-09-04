from app import db
from app.models.models import Employee
from app.Common.EmployeeReq import EmployeeReq
from flask import session
import json


class EmployeeRep:
    def __init__(self):
        self

    def createEmpAccount(self, employee: Employee):
        try:
            db.session.add(employee)  # Thêm nhân viên
            db.session.commit()  # Lưu lại
            return True
        except:
            return False  # Tạo thất bại

    def validateUser(self, userName: str, password: str):
        req = EmployeeReq()
        # import pdb
        # pdb.set_trace()
        result = Employee.query.filter(Employee.userName == userName.strip(),
                                       Employee.password == password.strip()).first()  # Lấy nhân viên theo username và password
        db.session.commit()  # Lưu lại
        # Gán giá trị trả về
        if result is None:
            # session["username"] = ""
            return {
                "data": "",
                "success": False
            }
        else:
            req._userName = result.userName
            req._password = result.password
            req._lastName = result.lastName
            req._firstName = result.firstName
            req._identityCard = result.identityCard
            req._phoneNumber = result.phoneNumber
            req._gender = result.gender
            req._birthDay = result.birthDay
            req._address = result.address
            req._note = result.note
            return {
                "data": req.__str__(),
                "success": True
            }
