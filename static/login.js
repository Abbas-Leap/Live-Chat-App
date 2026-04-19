document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    let visitorName = document.getElementById("visitorName");
    visitorName = visitorName.value.trim();
    // To block noise from server
    if (visitorName.length < 3 || visitorName.length > 15) {
        alert("Visitor name must be between 3 and 15 characters long");
        return;
    }

    let response = (await fetch('/loginComm', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "visitorName": visitorName })
    }));

    response = await response.json();

    if (response["status"] == "ok") {
        alert(response["msg"]);
        window.location.replace(`${window.location.origin}${response["url"]}`);
        return;
    }

    alert(`Error ${response["msg"]}`);
});
