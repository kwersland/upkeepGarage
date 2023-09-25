function display(pic, text) {
    document.getElementById(pic).style.display = "none";
    document.getElementById(text).style.display = "block";
}

function hide(pic, text) {
    document.getElementById(pic).style.display = "contents";
    document.getElementById(text).style.display = "none";
}