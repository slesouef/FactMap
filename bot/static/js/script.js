document.getElementById("submit").addEventListener("click", function () {
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        newPersonalMessage(entry);
        spinner();
        getData(entry);
    }
});

function newPersonalMessage(text) {
    var newEntry = document.createElement("div");
    newEntry.textContent = text;
    newEntry.className = "message message-personal";
    document.getElementById("messages").appendChild(newEntry);
}

function spinner() {
    var tempDiv = document.createElement("div");
    tempDiv.className = "message";
    tempDiv.id = "spinner";
    document.getElementById("messages").appendChild(tempDiv);
    var loader = document.createElement("div");
    loader.className = "spinner";
    document.getElementById("spinner").appendChild(loader);
}