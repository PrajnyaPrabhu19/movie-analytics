function exportDropDown() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      var s = $("<select id='exportSelector'/>");
      s.children().remove();
      data = JSON.parse(xhttp.responseText);

      console.log(data);

      for (var val in Object.keys(data)) {
        $("<option />", {
          text: Object.keys(data)[val],
          value: data[Object.keys(data)[val]],
        }).appendTo(s);
      }

      s.appendTo("#fileListHolder");
    }
  };
  xhttp.open("GET", "http://localhost:5000/exportList", true);
  xhttp.send();
}

function importFunctionality() {
  let url =
    "http://localhost:5000/importData?file_name=" +
    document.getElementById("exportSelector").value;
  console.log(url);
  var xhttp2 = new XMLHttpRequest();
  xhttp2.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      data = JSON.parse(xhttp2.responseText)["data"];
      console.log(data);
      go();
    }
  };
  xhttp2.open("GET", url, true);
  xhttp2.send();
}

function exportFunctionality() {
  let fileName = prompt();
  let url = "http://localhost:5000/exportData?file_name=" + fileName;
  console.log(url);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      data = JSON.parse(xhttp.responseText)["data"];
      console.log(data);
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}
