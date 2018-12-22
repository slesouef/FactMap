document.getElementById("submit").addEventListener("click", function () {
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        newPersonalMessage(entry);
        tempLoader();
        getData(entry, newBotMessage);
    }
});

function newPersonalMessage(text) {
    var newEntry = document.createElement("div");
    newEntry.textContent = text;
    newEntry.className = "message message-personal";
    document.getElementById("messages").appendChild(newEntry);
}

function newBotMessage(text) {
    var newResponse = document.createElement("div");
    newResponse.textContent = text;
    newResponse.className = "message";
    document.getElementById("messages").appendChild(newResponse);
    newResponse.scrollIntoView(false);
}

function tempLoader() {
    var tempDiv = document.createElement("div");
    tempDiv.className = "message";
    tempDiv.id = "spinner";
    tempDiv.innerHTML = "<div class=spinner></div>";
    document.getElementById("messages").appendChild(tempDiv);
}