function getData(entry, callback) {
    var req = new XMLHttpRequest();
    req.open("POST", "/data");
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText)
        } else {
            console.error(req.status + " " + req.statusText);
        }
    });
    req.addEventListener("error", function () {
        console.error("Network error");
    });
    req.send(entry);
}