function simpleGET(url) {
  var xhr3 = new XMLHttpRequest();
  xhr3.onreadystatechange = function () {
    if (xhr3.readyState == XMLHttpRequest.DONE) {
      //alert(xhr.responseText);
    }
  };
  xhr3.open("GET", url, true);
  xhr3.send();
}
