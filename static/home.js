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
