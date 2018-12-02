document.getElementById('confirm').addEventListener("click", function(){
    var entry = document.getElementById("question").value;
    document.getElementById("question").value = "";
    var new_entry = document.createElement("div");
    new_entry.textContent = entry;
    document.getElementById("messages").appendChild(new_entry);
});