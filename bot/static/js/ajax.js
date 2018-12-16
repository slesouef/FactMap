function getdata(){
    var req = new XMLHttpRequest();
    req.open("GET", "http://localhost:5000/data");
    req.addEventListener("load", function(){
        if(req.status >= 200 && req.status < 400){
            var new_response = document.createElement("div");
            new_response.textContent = req.responseText;
            new_response.className = "message";
            document.getElementById("messages").appendChild(new_response);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function(){
        console.error("Network error on " + url);
    });
    req.send(null);
}