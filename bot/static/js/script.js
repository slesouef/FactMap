document.getElementById("submit").addEventListener("click", function () {
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        newPersonalMessage(entry);
        tempLoader();
        getData(entry, createNewMap);
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
            getData(entry, createNewMap);
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

function createNewMap(text) {
    response = JSON.parse(text);
    var newMap = document.createElement("div");
    newMap.className = "message";
    newMap.innerHTML = "<div>" + response.address + "</div>" + "<div" +
        " id='map'></div>"
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newMap);
    initMap(response.coordinates[0], response.coordinates[1]);
    newMap.scrollIntoView(false);
}

function initMap(latitude, longitude) {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: latitude, lng: longitude},
        zoom: 13
    });
}

function newBotMessage(text) {
    var newResponse = document.createElement("div");
    newResponse.textContent = text;
    newResponse.className = "message";
    document.getElementById("spinner").outerHTML = "";
    document.getElementById("messages").appendChild(newResponse);
    newResponse.scrollIntoView(false);
}

function tempLoader() {
    var tempDiv = document.createElement("div");
    tempDiv.className = "message";
    tempDiv.id = "spinner";
    tempDiv.innerHTML = "<div class=spinner></div>";
    document.getElementById("messages").appendChild(tempDiv);
    tempDiv.scrollIntoView(false);
}