document.getElementById("submit").addEventListener("click", function(){
    var entry = document.getElementById("input").value;
    if (entry === '') {
        return false;
    } else {
        document.getElementById("input").value = "";
        var new_entry = document.createElement("div");
        new_entry.textContent = entry;
        new_entry.className = "message message-perso";
        document.getElementById("messages").appendChild(new_entry);
        getdata();
    }
});