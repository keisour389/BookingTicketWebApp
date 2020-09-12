const defaultURL = "http://127.0.0.1:5000";

var flightSchedule = {
    flightScheduleID: null,
    ticketClass: null
}
var ticket = {
    identityCard: null,
    phoneNumber: null,
    ticketClass: null,
    price: null,
    note: null,
    employeeID: null,
    customerID: null,
    flightSchedulesID: null
}
async function updateFlightSchedule() {
    flightSchedule.flightScheduleID = document.getElementById("flight-schedule-ID").innerHTML;
    flightSchedule.ticketClass = ticket.ticketClass = parseInt(document.getElementById("customerTicketType").value)
    await fetch(defaultURL + "/update-flight-schedule", {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.flightSchedule)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch((error) => {
            console.error(error);
        })

}
async function createTicket() {
    //Lấy userId trước khi tạo vé
    await this.getCusId()
        .then(result => {
            if (result.success) {
                //Lấy giá trị
                this.ticket.customerID = result.data.toString();
                //Tạo vé
                //DOM giá trị qua
                ticket.flightSchedulesID = document.getElementById("flight-schedule-ID").innerHTML;
                ticket.identityCard = document.getElementById("customerId").value;
                ticket.phoneNumber = document.getElementById("customerPhoneNumber").value;
                try {
                    ticket.ticketClass = parseInt(document.getElementById("customerTicketType").value);
                    ticket.price = parseInt(document.getElementById("price").innerHTML);
                }
                catch {
                    ticket.ticketClass = 0;
                    ticket.price = 0;
                }

                console.log(this.ticket);

                //Tạo vé
                fetch(defaultURL + "/create-ticket", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.ticket)
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.result) {
                            this.updateFlightSchedule(); //update số vé sau khi mua
                            alert("Chúc mừng bạn đã mua vé thành công !!!");
                            window.location.href = "/";
                        }
                        else {
                            alert("Mua vé không thành công.")
                        }
                        console.log(data.result)
                    })
                    .catch((error) => {
                        console.error(error);
                    })
            }
            else {
                alert("Lỗi xác thực người dùng");
            }
        })
        .catch((error) => {
            console.error(error);
        })
}
async function getCusId() {
    const response = await fetch(defaultURL + "/cus-session", {
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
        }
    });
    return response.json();
    // .then(data => {
    //     this.ticket.customerID = data.toString();
    //     console.log(this.ticket);
    // })
    // .catch((error) => {
    //     console.error(error);
    // })
}
//Hàm xử lí khi chọn loại vé
function chooseTicketType() {
    var value = document.getElementById("customerTicketType").value;
    if (value == 1) {
        //Bằng giá tiền hạng nhất
        document.getElementById("price").innerHTML = document.getElementById("first-class-price").innerHTML;
    }
    else {
        //Bằng giá tiền hạng nhất
        document.getElementById("price").innerHTML = document.getElementById("second-class-price").innerHTML;
    }
}