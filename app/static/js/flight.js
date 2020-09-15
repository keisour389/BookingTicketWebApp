function summit(){
    var x = document.getElementById("oneway").checked;
    if (x === true){
        document.getElementById("ngayve").style.display = "none"
    }
    else
        document.getElementById("ngayve").style.display = "inline"
}
