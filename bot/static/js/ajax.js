document.getElementById("button").addEventListener("click", function(e){
    e.preventDefault();
    var req = new XMLHttpRequest();
    req.open("GET", "http://localhost:5000/time");
    req.addEventListener("load", function(){
        if(req.status >= 200 && req.status < 400){
            document.getElementById("button").innerHTML = "<p>" + "<b>" +
                req.responseText + "</b>" + "</p>";
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function(){
        console.error("Network error on " + url);
    });
    req.send(null);
});