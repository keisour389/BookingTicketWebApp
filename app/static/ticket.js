const defaultURL = "http://127.0.0.1:5000";

var ticket = {
    identityCard: "123456",
    phoneNumber: "123456",
    ticketClass: 1,
    price: 1000000,
    note: None,
    employeeID: "1",
    customerID = "1",
    flightSchedulesID = "1"
}
async function createTicket(){
    await fetch(defaultURL + "/create-ticket", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: this.ticket
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .then(error => {
        console.error(error);
    })
}