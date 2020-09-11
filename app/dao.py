from app import db
from app.models import *


def create_ticker(identityCard, phoneNumber, ticketClass, price, note, employeeID, flightSchedulesID, customerID):
    ticket = Ticket()
    # Gán giá trị
    ticket.identityCard = identityCard
    ticket.phoneNumber = phoneNumber
    ticket.ticketClass = ticketClass
    ticket.price = price
    ticket.note = note
    ticket.employeeID = employeeID  # Lúc mới đặt vé mặc định là null
    ticket.flightSchedulesID = flightSchedulesID
    ticket.customerID = customerID
    # Tạo dữ liệu
    try:
        db.session.add(ticket)
        db.session.commit()  # Lưu lại
        return True
    except Exception as ex:
        return False


def create_cus(userName, password, lastName, firstName, identityCard, phoneNumber, birthDay, gender, address, note):
    cus = Customer()
    cus.userName = userName
    cus.password = password
    cus.lastName = lastName
    cus.firstName = firstName
    cus.identityCard = identityCard
    cus.phoneNumber = phoneNumber
    cus.birthDay = birthDay
    cus.gender = gender
    cus.address = address
    cus.note = note
    try:
        db.session.add(cus)
        db.session.commit()  # Lưu lại
        return True
    except Exception as ex:
        return False


def validate_user(username, password):
    user = Customer.query.filter(Customer.userName == username,
                                 Customer.password == password).first()
    if user:
        return user
    else:
        user = Employee.query.filter(Employee.userName == username,
                                     Employee.password == password).first()
        return user
