new EventSource('/events').onmessage = function (e) {
    let messageElement = document.createElement('p');
    messageElement.textContent = e.data;
    messageElement.id = "message";

    document.getElementById("messageArea").prepend(messageElement);
};

async function fetchHistory() {
    try {
        let response = await fetch('/history');

        if (!response.ok) {
            throw new Error("Error");
        }

        let data = await response.json();

        for (let i of data) {
            let messageElement = document.createElement('p');
            messageElement.textContent = i;
            messageElement.id = "message";

            document.getElementById("messageArea").prepend(messageElement);
        }

    } catch (Error) {
        alert("Error fetching data");
    }
}

document.addEventListener("DOMContentLoaded", fetchHistory);

async function sendMessage() {
    const formData = new FormData(document.getElementById("Input"));

    if (!document.getElementById("InputText").value)
        return;

    let response = fetch('/submit', {
        method: "POST",
        body: formData
    });

    document.getElementById("InputText").value = "";
}
