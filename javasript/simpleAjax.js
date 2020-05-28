var loadedData = [];
function loadDoc(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       loadedData.push(this.responseText);
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}
