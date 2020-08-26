from flask import jsonify
from app.Common.EmployeeReq import EmployeeReq
from app.DAL.EmployeeRep import EmployeeRep
from app.models.models import Employee
from app.models import models
import json
from app import db
from app.models import models

def createEmpAccount(empAccountReq: EmployeeReq):
    employeeRep = EmployeeRep() #DAL
    employeeAccount = Employee() #Bảng
    #Gán
    employeeAccount.userName = empAccountReq.userName
    employeeAccount.password = empAccountReq.password
    employeeAccount.firstName = empAccountReq.firstName
    employeeAccount.lastName = empAccountReq.lastName
    employeeAccount.identityCard = empAccountReq.identityCard
    employeeAccount.phoneNumber = empAccountReq.phoneNumber
    employeeAccount.birthDay = empAccountReq.birthDay
    employeeAccount.gender = empAccountReq.gender
    employeeAccount.address = empAccountReq.address
    employeeAccount.note = empAccountReq.note
    #Tạo
    state = employeeRep.createEmpAccount(employeeAccount)
    data = {"userName": empAccountReq.userName,
            "password": empAccountReq.password,
            "firstName": empAccountReq.firstName,
            "lastName": empAccountReq.lastName,
            "identityCard": empAccountReq.identityCard,
            "phoneNumber": empAccountReq.phoneNumber,
            "birthDay": empAccountReq.birthDay,
            "gender": empAccountReq.gender,
            "address": empAccountReq.address,
            "note": empAccountReq.note}
    result = {
        "data": data,
        "success": state
    }

    return result

def validateUser(userName: str, password: str):
    employeeRep = EmployeeRep() #DAL
    result = employeeRep.validateUser(userName, password)
    return result
