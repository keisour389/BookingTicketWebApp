from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


# class ở PY đặt tên theo chuẩn Lạc Đà Hoa
# Kế thừa db.Model để hiểu đây là 1 table
# Lớp này sẽ ánh xạ xuống database để tạo bảng theo tên class
class Category(db.Model):  # Đây là cú pháp kế thừa trong PY
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Khóa chính tự động tăng
    name = Column(String(50), nullable=False)
    # Chỉ ra là bảng category có quan hệ với product
    # backref tự động thêm vào bảng product 1 thuộc tính category. Khi đó ở product có thể gọi được category
    products = relationship('Product', backref='category', lazy=True)

    # Giống hàm ghi đè toString() của Java
    def _str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Khóa chính tự động tăng
    name = Column(String(50), nullable=False)
    description = Column(String(50), nullable=True)
    price = Column(Float, default=0)  # Giá trị mặc định là 0
    image = Column(String(255), nullable=True)
    # Tạo khóa ngoại
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    # Giống hàm ghi đè toString() của Java
    def _str__(self):
        return self.name


# Câu lệnh tạo bảng dưới database
if __name__ == "__main__":
    db.create_all()

# Các câu lệnh tương tác với CSDL
# Thêm: db.session.add(c1) với c1 là bảng với các trường giá trị
# Lấy: Product.query.get(1) với 1 là khóa chính của bảng product
# Lọc dữ liệu: Product.query.filter()
# Lấy tất cả dữ liệu: Product.query.all()
# Lưu lại thay đổi:db.session.commit()
