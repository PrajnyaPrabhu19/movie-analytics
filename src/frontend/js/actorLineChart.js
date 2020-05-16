function generateActor(actor) {
  google.charts.load("current", { packages: ["line"] });
  google.charts.setOnLoadCallback(drawLineChart(actor));

  function drawLineChart(actor) {
    $.ajax({
      url: "http://127.0.0.1:5000/ActorTrajectory?actor=" + actor,
      dataType: "json",
      type: "GET",
      contentType: "application/json; charset=utf-8",
      success: function (data) {
        var dirTrajectory = [["Year", "Revenue"]]; // Define an array and assign columns for the chart.

        // Loop through each data and populate the array.
        $.each(data["data"], function (index, value) {
          dirTrajectory.push([value.year, value.revenue]);
        });

        // Set chart Options.
        var options = {
          chart: {
            title: "Director Career Trajectory",
            subtitle: "--",
          },
          axes: {
            x: {
              0: { side: "bottom" }, // Use "top" or "bottom".
            },
          },
        };

        // Create DataTable and add the array to it.
        var figures = google.visualization.arrayToDataTable(dirTrajectory);

        // Define the chart type (LineChart) and the container (a DIV in our case).
        var chart = new google.charts.Line(document.getElementById("chart1"));

        // Draw the chart with Options.
        chart.draw(figures, google.charts.Line.convertOptions(options));
      },
      error: function (XMLHttpRequest, textStatus, errorThrown) {
        alert("Got an Error");
      },
    });
  }
}
