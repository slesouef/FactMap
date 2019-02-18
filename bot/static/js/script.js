document.getElementById("submit").addEventListener("click", function () {
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        newPersonalMessage(entry);
        tempLoader();
        getData(entry, checkResponse);
    }
});

document.getElementById("input").addEventListener("keyup", function (e) {
    if (e.key === 'Enter') {
        var entry = document.getElementById("input").value;
        if (entry === '\n') {
            return false;
        } else {
            document.getElementById("input").value = "";
            newPersonalMessage(entry);
            tempLoader();
            getData(entry, checkResponse);
        }
    }
});

function newPersonalMessage(text) {
    var newEntry = document.createElement("div");
    newEntry.textContent = text;
    newEntry.className = "message message-personal";
    document.getElementById("messages").appendChild(newEntry);
    newEntry.scrollIntoView(true);
}

function tempLoader() {
    var tempDiv = document.createElement("div");
    tempDiv.className = "message";
    tempDiv.id = "spinner";
    tempDiv.innerHTML = "<div class=spinner></div>";
    document.getElementById("messages").appendChild(tempDiv);
    tempDiv.scrollIntoView(true);
}

function checkResponse(body) {
    var response = JSON.parse(body);
    if (response.error === "empty parse return"){
        noQuestionMessage();
    } else {
        createNewReply(body);
    }
}

function noQuestionMessage() {
    var newMessage = document.createElement("div");
    newMessage.className = "message";
    newMessage.textContent = "Désolé, je n'ai pas compris ta question." +
        " Peux-tu répéter s'il te plaît?";
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newMessage);
    newMessage.scrollIntoView(true);
}

function createNewReply(body) {
    var response = JSON.parse(body);
    var newReply = document.createElement("div");
    var breakline = document.createElement("br");
    var address = createAddress(response.map.address);
    var map = createMap();
    if (response.map.status !== "OK") {
        noLocationMessage();
    } else if (response.wiki.status !== "OK") {
        var noExtract = noKnowledgeMessage();
        newReply.className = "message";
        newReply.appendChild(address);
        newReply.appendChild(breakline);
        newReply.appendChild(map);
        newReply.appendChild(breakline);
        newReply.appendChild(noExtract);
    } else {
        var extract = createKnowledge(response.wiki);
        newReply.className = "message";
        newReply.appendChild(address);
        newReply.appendChild(breakline);
        newReply.appendChild(map);
        newReply.appendChild(breakline);
        newReply.appendChild(extract);
    }
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newReply);
    initMap(response.map.coordinates[0], response.map.coordinates[1]);
    incrementCounter();
    newReply.scrollIntoView(true);
}

function createAddress(text) {
    var newEntry = document.createElement("div");
    newEntry.textContent = "Cela se trouve à l’adresse suivante: " + text;
    return newEntry;
}

function noLocationMessage() {
    var newMessage = document.createElement("div");
    newMessage.className = "message";
    newMessage.textContent = "Désolé, je doit avoir une poussée d’Alzheimer" +
        " précoce. Je ne me souvient plus où ça se trouve.";
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newMessage);
    newMessage.scrollIntoView(true);
}

counter = 0;
function incrementCounter() {
    counter += 1;
}

function createMap() {
    var newMap = document.createElement("div");
    newMap.id = "map" + counter;
    newMap.class="map";
    return newMap;
}

function createKnowledge(response) {
    var text = response.extract;
    var url = response.URL;
    var newEntry = document.createElement("div");
    newEntry.innerHTML = "Est-ce que je t'ai déjà parlé de cet endroit où" +
        " j’ai pas mal traîné mes guêtres? " + text +
        " [ <a href='" + url + "'>Plus d'information sur Wikipedia</a> ]";
    return newEntry;
}

function noKnowledgeMessage() {
    var newMessage = document.createElement("div");
    newMessage.textContent = "Désolé, mais je ne sais rien sur cet endroit";
    return newMessage;
}

function initMap(latitude, longitude) {
    var location = {lat: latitude, lng: longitude};
    var mapID = "map" + counter;
    var map = new google.maps.Map(document.getElementById(mapID), {
        center: location,
        zoom: 12
    });
    var marker = new google.maps.Marker({
        position: location,
        map : map
    });
}
