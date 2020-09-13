from app import dao, app
import csv
from datetime import datetime
import os


def export_csv():
    data = dao.get_bookingdetails()
    p = os.path.join(app.root_path, "data/report-%s.csv" % str(datetime.now()))
    if data:
        with open(p, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["bookingID", "identityCard", "phoneNumber", "ticketClass", "price",
                                                   "note", "flightSchedulesID", "customerID", "employeeID"])
            writer.writeheader()
            for d in data:
                writer.writerow(d)
        return p
    else:
        with open(p, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Status"])
            writer.writerow({"Status": "No data"})
        return p
