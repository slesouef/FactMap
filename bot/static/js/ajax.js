document.getElementById("button").addEventListener("click", function(){
  // e.preventDefault;
  var req = new XMLHttpRequest();
  req.open("GET", "http://localhost:5000/time");
  req.addEventListener("load", function(){
    if(req.status >= 200 && req.status < 400){
      console.log(req.responseText);
    } else {
      console.error(req.status + " " + req.statusText + " " + url);
    };
  });
  req.addEventListener("error", function(){
    console.error("Erreur reseau avec l'url " + url);
  });
  req.send(null);
})