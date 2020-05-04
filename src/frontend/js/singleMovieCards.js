function singelMovieCards() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      data = JSON.parse(xhttp.responseText);

      for (var i = 0; i < data.length; i++) {
        let imdb_id = data[i]["imdb_id"];
        let movie_title = data[i]["original_title"];
        let tagline = data[i]["tagline"];
        let formatValue = d3.format(".2s");
        let loss = formatValue(data[i]["loss"]).replace("M", " Million$");
        let director = data[i]["director"];
        console.log(data[i]["genres"]);
        let genre_list = data[i]["genres"];
        let genre_badges = "";

        for (var j = 0; j < genre_list.length; j++) {
          genre_badges +=
            ' <span class="badge badge-primary">' + genre_list[j] + "</span>";
        }

        $("#wmovie").append(
          '<div class="media">\
             \
                <img src="http://img.omdbapi.com/?i=' +
            imdb_id +
            '&apikey=a238dc08" class="align-self-start mr-3" height="150" width="100" alt="...">\
                <div class="media-body">\
                <div class="card-title"><h4><strong>' +
            movie_title +
            "</strong></h4> <strong>Directed by:</strong> " +
            director.replace("|", ", ") +
            ' \
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
            \
  \
         "
        );
      }
    }
  };

  xhttp.open(
    "GET",
    "http://localhost:5000/searchFlopMovies?search_year=",
    true
  );
  xhttp.send();

  var xhttp1 = new XMLHttpRequest();
  xhttp1.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      movies = JSON.parse(xhttp1.responseText);

      for (var i = 0; i < movies.length; i++) {
        let imdb_id = movies[i]["imdb_id"];
        let movie_title = movies[i]["original_title"];
        let tagline = movies[i]["tagline"];
        let formatValue = d3.format(".2s");
        let profit = formatValue(movies[i]["profit"]).replace(
          "G",
          " Billion $"
        );
        let director = movies[i]["director"];
        console.log(movies[i]["genres"]);
        let genre_list = movies[i]["genres"];
        let genre_badges = "";

        for (var j = 0; j < genre_list.length; j++) {
          genre_badges +=
            ' <span class="badge badge-primary">' + genre_list[j] + "</span>";
        }

        $("#bmovie").append(
          '<div class="media">\
             \
                <img src="http://img.omdbapi.com/?i=' +
            imdb_id +
            '&apikey=a238dc08" class="align-self-start mr-3" height="150" width="100" alt="...">\
                <div class="media-body">\
                <div class="card-title"><h4><strong>' +
            movie_title +
            "</strong></h4> <strong>Directed by:</strong> " +
            director.replace("|", ", ") +
            ' \
                <span class="badge badge-success"> + ' +
            profit +
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
            \
  \
         "
        );
      }
    }
  };
  xhttp1.open(
    "GET",
    "http://localhost:5000/highestGrossingMovie?search_year=",
    true
  );
  xhttp1.send();
}
