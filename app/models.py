from flask_admin import BaseView, expose
from flask import redirect
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, logout_user #Tạo user MixIn vào các user để đăng nhập
from app import db, admin #Truyền biến admin từ _init_

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
    #
    airport = relationship("FlightSchedules", secondary="intermediary_airport", lazy="subquery",
                           backref=backref("Airport", lazy=True))


class Customer(db.Model, UserMixin):
    __tablename__ = "customer"

    userName = Column(String(20), primary_key=True)
    password = Column(String(100), nullable=False)
    lastName = Column(String(20), nullable=False)
    firstName = Column(String(40), nullable=False)
    identityCard = Column(String(15), nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    birthDay = Column(Date, nullable=False)
    gender = Column(String(5), nullable=False)
    address = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

class Employee(db.Model, UserMixin):
    __tablename__ = "employee"

    userName = Column(String(20), primary_key=True)
    password = Column(String(100), nullable=False)
    lastName = Column(String(20), nullable=False)
    firstName = Column(String(40), nullable=False)
    identityCard = Column(String(15), nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    birthDay = Column(Date, nullable=False)
    gender = Column(String(5), nullable=False)
    address = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

    def get_id(self):
        return self.userName
    def __str__(self):
        return self.userName

class FlightSchedules(db.Model):
    __tablename__ = "flight_schedules"

    flightSchedulesID = Column(String(30), primary_key=True)
    flightDateTime = Column(DateTime, nullable=False)
    flightTotalTime = Column(Float, nullable=False)
    firstClassAmount = Column(Integer, nullable=False)
    secondClassAmount = Column(Integer, nullable=False)
    firstClassPrice = Column(Float, nullable=False)
    secondClassPrice = Column(Float, nullable=False)
    note = Column(String(255), nullable=True)
    #Tạo khóa ngoại
    airportToTakeOff = Column(String(10), ForeignKey(Airport.airportID), nullable=False)
    airportToLanding = Column(String(10), ForeignKey(Airport.airportID), nullable=False)
    #
    airport = relationship("Airport", secondary="intermediary_airport", lazy="subquery",
                           backref=backref("flight_schedules", lazy=True))

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
    employeeID = Column(String(20), ForeignKey(Employee.userName), nullable=True)

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

#Khi lấy tên bảng trong dấu '' phải lấy đúng theo __tablename__
#Bảng quan hệ nhiều - nhiều của sân bay và lịch chuyến bay
intermediary_airport = db.Table('intermediary_airport',
                               Column('flightSchedulesID', String(30),
                                      ForeignKey('flight_schedules.flightSchedulesID'), primary_key=True),
                               Column('airportID', String(10),
                                      ForeignKey('airport.airportID'), primary_key=True),
                               Column('totalTimeToStop', Float, nullable=False),
                               Column('note', String(255), nullable=False)
                               )

# class IntermediaryAirport(db.Model):
#     __tablename__ = "intermediaryairport"
#
#     #Khóa chính và khóa ngoại
#     flightSchedulesID = Column(String(30), ForeignKey(FlightSchedules.flightSchedulesID), primary_key=True)
#     airportID = Column(String(10), ForeignKey(Airport.airportID), primary_key=True)
#
#     totalTimeToStop = Column(Float, nullable=False)
#     note = Column(String(255), nullable=True)

class EmployeeModelView(ModelView):
    column_display_pk = True #Cho tạo khóa
    can_create = True
    form_columns = ('userName', 'password','lastName', 'firstName', 'identityCard',
                    'phoneNumber', 'birthDay', 'gender', 'address', 'note')

    def is_accessible(self):
        return current_user.is_authenticated #Nếu chưa đăng nhập thì không cho vô

class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin") #Quay về trang chủ
#Thêm cái view vào
#Trước khi create lại db phải tắt cái admin
admin.add_view(EmployeeModelView(Employee, db.session))
admin.add_view(ModelView(Airport, db.session))
admin.add_view(LogoutView(name="Logout"))
#Câu lệnh tạo bảng dưới database
if __name__ == "__main__":
     db.create_all()