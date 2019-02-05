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

document.getElementById("input").addEventListener("keydown", function (e) {
    if (e.key === 'Enter') {
        var entry = document.getElementById("input").value;
        if (entry === '') {
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
    newEntry.scrollIntoView(false);
}

function tempLoader() {
    var tempDiv = document.createElement("div");
    tempDiv.className = "message";
    tempDiv.id = "spinner";
    tempDiv.innerHTML = "<div class=spinner></div>";
    document.getElementById("messages").appendChild(tempDiv);
    tempDiv.scrollIntoView(false);
}

function checkResponse(body) {
    var response = JSON.parse(body);
    if (response.error === "empty parse return"){
        noQuestionMessage();
    } else if (response.status !== "OK") {
        noMapMessage();
    } else {
        createNewReply(body);
    }
}

function noQuestionMessage() {
    var newMessage = document.createElement("div");
    newMessage.className = "message";
    newMessage.textContent = "Je n'ai pas compris ta question. Tu peux" +
        " repeter s'il te plait?";
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newMessage);
    newMessage.scrollIntoView(false);
}

function noMapMessage() {
    var newMessage = document.createElement("div");
    newMessage.className = "message";
    newMessage.textContent = "J'ai une poussée d'alzheimer précoce. Je ne me" +
        " souvient plus ou ca se trouve.";
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newMessage);
    newMessage.scrollIntoView(false);
}

counter = 0;
function incrementCounter() {
    counter += 1;
}

function createNewReply(body) {
    var response = JSON.parse(body);
    var newReply = document.createElement("div");
    var address = createAddress(response.address);
    var map = createMap();
    newReply.className = "message";
    newReply.appendChild(address);
    newReply.appendChild(map);
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newReply);
    initMap(response.coordinates[0], response.coordinates[1]);
    incrementCounter();
    newReply.scrollIntoView(false);
}

function createAddress(text) {
    var newEntry = document.createElement("div");
    newEntry.textContent = text;
    return newEntry;
}

function createMap() {
    var newMap = document.createElement("div");
    newMap.id = "map" + counter;
    newMap.class="map";
    return newMap;
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
