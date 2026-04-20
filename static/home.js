document.addEventListener("DOMContentLoaded", async function () {
    data = await getData();

    let visitorNameDisplay = document.getElementById("visitorName");

    visitorNameDisplay.textContent = data["visitorName"];

    if (data["messages"].length == 0) {
        alert("No messages to load");
        return;
    }

    for (let message of data["messages"]) {
        loadMessage(message);
    }

});

document.addEventListener("submit", async function (event) {
    event.preventDefault();
    // Get message and remove white space
    let message = document.getElementById("sendMessageInp");
    message = message.value.trim();
    // Filter noise
    if (message.length < 1 || message.length > 100) {
        alert("Message should be between 1 and 100 characters");
        return;
    }
    // Send it via /homeCommSendMessage
    let response = await fetch("/homeCommSendMessage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "message": message })
    });
    // Get the response from server
    response = await response.json();

    if (response["status"] == "ok")
        return;

    alert(response["message"]);
});

async function getData() {
    let response = (await fetch('/homeCommOneTime', {
        method: "POST"
    }));
    response = await response.json();

    return response;
}

function loadMessage(message) {
    let node = document.createElement("p");
    node.id = "Message";
    node.textContent = message;

    document.getElementById("messageArea").prepend(node);
}
