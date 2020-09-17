from app import app
from app import db
from app.models import *
import hashlib


def update_flight_schedules(flightScheduleID, ticketClass):
    try:
        flightSchedule = FlightSchedules.query.filter(FlightSchedules.flightSchedulesID == flightScheduleID).first()
        if ticketClass == 1:
            flightSchedule.firstClassAmount -= 1
        else:
            flightSchedule.secondClassAmount -= 1
        db.session.commit()
        return True
    except:
        return False


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
    hashpass = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
    cus.userName = userName
    cus.password = hashpass
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
        db.session.commit()
        return True
    except Exception as ex:
        return False


def validate_user_cus(username, password):
    hashpass = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
    user = Customer.query.filter(Customer.userName == username,
                                 Customer.password == hashpass).first()
    if user:
        return user
    return None


def validate_user_emp(username, password):
    user = Employee.query.filter(Employee.userName == username,
                                 Employee.password == password).first()
    if user:
        return user
    return None


def get_bookingdetails():
    data = Booking.query.all()
    if data:
        return data
    else:
        return None
