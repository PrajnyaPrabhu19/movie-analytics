function loadWorstMoviesList() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      data = JSON.parse(xhttp.responseText)["data"];

      for (var i = 0; i < data.length; i++) {
        let imdb_id = data[i]["imdb_id"];
        let movie_title = data[i]["original_title"];
        let tagline = data[i]["tagline"];
        let formatValue = d3.format(".2s");
        let loss = formatValue(data[i]["loss"]).replace("M", " M$");
        let director = data[i]["director"];
        console.log(data[i]["genres"]);
        let genre_list = data[i]["genres"];
        let genre_badges = "";

        for (var j = 0; j < genre_list.length; j++) {
          genre_badges +=
            ' <span class="badge badge-primary">' + genre_list[j] + "</span>";
        }

        $("#wmovieList").append(
          '<div class="card  text-dark bg-light pt-1 pb-1 pl-1 pr-1 mb-1" style="max-width: 36rem;">\
\
            <div class="media">\
           \
              <img src="http://img.omdbapi.com/?i=' +
            imdb_id +
            '&apikey=a238dc08" class="align-self-start mr-3" height="150" width="100" alt="...">\
              <div class="media-body">\
              <h5 class="card-title"><strong>' +
            movie_title +
            "</strong>( " +
            director.replace("|", ", ") +
            ' )</h5>\
              <span class="badge badge-danger"> - ' +
            loss +
            "</span>" +
            genre_badges +
            '\
              <p class="card-text"> Tagline:\
               ' +
            tagline +
            "</p>\
            </div>\
            </div>\
\
          </div>\
\
       "
        );
      }
    }
  };
  xhttp.open(
    "GET",
    "http://localhost:5000/searchFlopMovies?search_year=2015",
    true
  );
  xhttp.send();
}

function load3WorstMovies() {
  let year = $("#yearDropdown1").val();

  var xhr3 = new XMLHttpRequest();
  xhr3.onreadystatechange = function () {
    if (xhr3.readyState == XMLHttpRequest.DONE) {
      data = JSON.parse(xhr3.responseText)["data"];
      $("#worstMovieModalList").empty();
      for (var i = 0; i < 3; i++) {
        let imdb_id = data[i]["imdb_id"];
        let movie_title = data[i]["original_title"];
        let tagline = data[i]["tagline"];
        let formatValue = d3.format(".2s");
        let loss = formatValue(data[i]["loss"]).replace("M", " M$");
        let director = data[i]["director"];
        console.log(data[i]["genres"]);
        let genre_list = data[i]["genres"];
        let genre_badges = "";

        for (var j = 0; j < 3; j++) {
          genre_badges +=
            ' <span class="badge badge-primary">' + genre_list[j] + "</span>";
        }

        $("#worstMovieModalList").append(
          '<div class="row ml-2 mt-1"> <div class="card  text-dark bg-light pt-1 pb-1 pl-1 pr-1 mb-1" style="width: 30rem;">\
      \
              <div class="media">\
             \
                <img src="http://img.omdbapi.com/?i=' +
            imdb_id +
            '&apikey=a238dc08" class="align-self-start mr-3" height="160" width="110" alt="...">\
                <div class="media-body">\
                <h5 class="card-title"><strong>' +
            movie_title +
            "</strong>( " +
            director.replace("|", ", ") +
            ' )</h5>\
                <span class="badge badge-danger"> - ' +
            loss +
            "</span>" +
            genre_badges +
            '\
                <p class="card-text"> Tagline:\
                 ' +
            tagline +
            "</p>\
              </div>\
              </div>\
      \
            </div></div>\
      \
         "
        );
      }
    }
  };
  xhr3.open(
    "GET",
    "http://localhost:5000/searchFlopMovies?search_year=" + year,
    true
  );
  xhr3.send();
}
