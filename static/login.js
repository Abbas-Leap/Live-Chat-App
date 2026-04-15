document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    let visitorName = document.getElementById("visitorName");
    // To block noise from server
    if (visitorName.value.length < 3) {
        alert("Visitor name must be atleast 3 characters long");
        return;
    }

    let response = (await fetch('/loginComm', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "visitorName": visitorName.value })
    }));

    response = await response.json();

    if (response["status"] == "ok") {
        alert(response["msg"]);
        window.location.replace(`${window.location.origin}${response["url"]}`);
        return;
    }

    alert(`Error ${response["msg"]}`);
});
