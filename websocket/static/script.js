const socket = new WebSocket("ws://" + location.host + "/sync");

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    document.getElementById("valueDisplay").innerText = data.value;
};

function sendPlus() {
    socket.send(JSON.stringify({ action: "plus" }));
}

function sendMinus() {
    socket.send(JSON.stringify({ action: "minus" }));
}
