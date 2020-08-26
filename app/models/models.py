from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db

#class ở PY đặt tên theo chuẩn Lạc Đà Hoa
#Kế thừa db.Model để hiểu đây là 1 table
#Lớp này sẽ ánh xạ xuống database để tạo bảng theo tên class
class Airport(db.Model):
    __tablename__ = "airport"

    airportID = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)
    runway = Column(Integer, nullable=False)
    airportType = Column(String(50), nullable=False)
    address = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

class Customer(db.Model):
    __tablename__ = "customer"

    userName = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    lastName = Column(String(20), nullable=False)
    firstName = Column(String(40), nullable=False)
    identityCard = Column(String(15), nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    birthDay = Column(Date, nullable=False)
    gender = Column(String(5), nullable=False)
    address = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

class Employee(db.Model):
    __tablename__ = "employee"

    userName = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    lastName = Column(String(20), nullable=False)
    firstName = Column(String(40), nullable=False)
    identityCard = Column(String(15), nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    birthDay = Column(Date, nullable=False)
    gender = Column(String(5), nullable=False)
    address = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

class FlightSchedules(db.Model):
    __tablename__ = "flightschedules"

    flightSchedulesID = Column(String(30), primary_key=True)
    flightDateTime = Column(DateTime, nullable=False)
    flightTotalTime = Column(Float, nullable=False)
    firstClassAmount = Column(Integer, nullable=False)
    secondClassAmount = Column(Integer, nullable=False)
    note = Column(String(255), nullable=True)
    #Tạo khóa ngoại
    airportToTakeOff = Column(String(10), ForeignKey(Airport.airportID), nullable=False)
    airportToLanding = Column(String(10), ForeignKey(Airport.airportID), nullable=False)

class Ticket(db.Model):
    __tablename__ = "ticket"

    ticketID = Column(Integer, primary_key=True, autoincrement=True) #Khóa chính tự động tăng
    identityCard = Column(String(15), nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    ticketClass = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    note = Column(String(255), nullable=True)
    #Tạo khóa ngoại
    flightSchedulesID = Column(String(30), ForeignKey(FlightSchedules.flightSchedulesID), nullable=False)
    customerID = Column(String(20), ForeignKey(Customer.userName), nullable=False)
    employeeID = Column(String(20), ForeignKey(Employee.userName), nullable=False)

class BookingDetails(db.Model):
    __tablename__ = "bookingdetails"

    bookingID = Column(Integer, primary_key=True, autoincrement=True) #Khóa chính tự động tăng
    identityCard = Column(String(15), nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    ticketClass = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    note = Column(String(255), nullable=True)
    # Tạo khóa ngoại
    flightSchedulesID = Column(String(30), ForeignKey(FlightSchedules.flightSchedulesID), nullable=False)
    customerID = Column(String(20), ForeignKey(Customer.userName), nullable=False)
    employeeID = Column(String(20), ForeignKey(Employee.userName), nullable=False)

#Bảng quan hệ nhiều - nhiều của sân bay và lịch chuyến bay
class IntermediaryAirport(db.Model):
    __tablename__ = "intermediaryairport"

    #Khóa chính và khóa ngoại
    flightSchedulesID = Column(String(30), ForeignKey(FlightSchedules.flightSchedulesID), primary_key=True)
    airportID = Column(String(10), ForeignKey(Airport.airportID), primary_key=True)

    totalTimeToStop = Column(Float, nullable=False)
    note = Column(String(255), nullable=True)

#Câu lệnh tạo bảng dưới database
if __name__ == "__main__":
     db.create_all()