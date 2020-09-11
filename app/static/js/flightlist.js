const defaultURL = "http://127.0.0.1:5000";

var ticket = {
    identityCard: null,
    phoneNumber: null,
    ticketClass: null,
    price: 1000000,
    note: null,
    employeeID: "1",
    customerID: "1",
    flightSchedulesID: "1"
}
async function createTicket(){
    //DOM giá trị qua
    ticket.identityCard = document.getElementById("customerId").value;
    ticket.phoneNumber = document.getElementById("customerPhoneNumber").value;
    try{
        ticket.ticketClass = parseInt(document.getElementById("customerTicketType").value);
        ticket.price = parseInt(document.getElementById("price").innerHTML);
    }
    catch{
        ticket.ticketClass = 0;
        ticket.price = 0;
    }
    
    console.log(this.ticket);

    await fetch(defaultURL + "/create-ticket", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.ticket)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert("Chúc mừng bạn đã mua vé thành công !!!");
        window.location.href = "/";
    })
    .catch((error) => {
        console.error(error);
    })
}