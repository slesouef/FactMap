function getData(entry, callback) {
    var req = new XMLHttpRequest();
    req.open("POST", "/data");
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText)
        } else {
            console.error(req.status + " " + req.statusText);
            displayFatalErrorMessage();
        }
    });
    req.addEventListener("error", function () {
        console.error("Network error");
        displayFatalErrorMessage();
    });
    req.send(entry);
}

function displayFatalErrorMessage() {
    var newMessage = document.createElement("div");
    newMessage.className = "message";
    newMessage.textContent = "Désolé, j'ai besoin de me reposer tout d'un" +
        " coup. Si tu veux bien, on reprendra ca un autre jour.";
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newMessage);
    newMessage.scrollIntoView(false);
}
