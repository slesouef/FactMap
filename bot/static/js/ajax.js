function getData(entry, callback) {
    var req = new XMLHttpRequest();
    req.open("POST", "http://localhost:5000/data");
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText)
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Network error on " + url);
    });
    req.send(entry);
}