document.getElementById("submit").addEventListener("click", function () {
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        newPersonalMessage(entry);
        getData(entry);
    }
});

function newPersonalMessage(text) {
    var newEntry = document.createElement("div");
    newEntry.textContent = text;
    newEntry.className = "message message-personal";
    document.getElementById("messages").appendChild(newEntry);
}
