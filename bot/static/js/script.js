document.getElementById("submit").addEventListener("click", function () {
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        var newEntry = document.createElement("div");
        newEntry.textContent = entry;
        newEntry.className = "message message-personal";
        document.getElementById("messages").appendChild(newEntry);
        getData(entry);
    }
});