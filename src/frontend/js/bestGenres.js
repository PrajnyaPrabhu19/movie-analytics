function loadbestGenres() {
  const svg = d3.select("svg"),
    margin = { top: 20, right: 20, bottom: 30, left: 50 },
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    x = d3.scaleBand().rangeRound([0, width]).padding(0.2),
    y = d3.scaleLinear().rangeRound([height, 0]),
    g = svg
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

  d3.json("http://localhost:5000/analyticsGrenre?search_year=")
    .then((data) => {
      data = data.RECORDS;

      x.domain(data.map((d) => d.genre_type));
      y.domain([0, d3.max(data, (d) => d.total_amt)]);

      g.append("g")
        .attr("class", "axis axis-x")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x));

      formatValue = d3.format("~s");

      g.append("g")
        .attr("class", "axis axis-y")
        .call(
          d3
            .axisLeft(y)
            .ticks(10)
            .tickSize(8)
            .tickFormat(function (d) {
              return formatValue(d).replace("G", " B$");
            })
        );

      g.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", (d) => x(d.genre_type))
        .attr("y", (d) => y(d.total_amt))
        .attr("width", x.bandwidth())
        .attr("height", (d) => height - y(d.total_amt));
    })
    .catch((err) => {
      svg
        .append("text")
        .attr("y", 20)
        .attr("text-anchor", "left")
        .style("font-size", "20px")
        .style("font-weight", "bold")
        .text(`Couldn't open the data file: "${err}".`);
    });
}
