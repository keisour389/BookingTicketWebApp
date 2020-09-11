from app import db
from app.models import *

def create_ticker(identityCard, phoneNumber, ticketClass, price, note, employeeID, flightSchedulesID, customerID):
    ticket = Ticket()
    #Gán giá trị
    ticket.identityCard = identityCard
    ticket.phoneNumber = phoneNumber
    ticket.ticketClass = ticketClass
    ticket.price = price
    ticket.note = note
    ticket.employeeID = employeeID #Lúc mới đặt vé mặc định là null
    ticket.flightSchedulesID = flightSchedulesID
    ticket.customerID = customerID
    #Tạo dữ liệu
    try:
        db.session.add(ticket)
        db.session.commit() #Lưu lại
        return True
    except Exception as ex:
        return False