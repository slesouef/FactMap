function getData(entry) {
    var req = new XMLHttpRequest();
    req.open("POST", "http://localhost:5000/data");
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            var newResponse = document.createElement("div");
            newResponse.textContent = req.responseText;
            newResponse.className = "message";
            document.getElementById("messages").appendChild(newResponse);
            newResponse.scrollIntoView(false);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Network error on " + url);
    });
    req.send(entry);
}