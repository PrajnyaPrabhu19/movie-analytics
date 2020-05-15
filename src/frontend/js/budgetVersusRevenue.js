function loadBudgetVsRevenue() {
  var data;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      data = JSON.parse(xhttp.responseText);

      models = data["data"].map((i) => {
        i.year = i.year;
        return i;
      });

      color = d3.scaleOrdinal().range(["#d0743c", "red"]);

      var container = d3.select("#d3id"),
        width = 1200,
        height = 500,
        margin = { top: 30, right: 30, bottom: 30, left: 50 },
        barPadding = 0.2,
        axisTicks = { qty: 5, outerSize: 0, dateFormat: "%m-%d" };

      var svg = container
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      var xScale0 = d3
        .scaleBand()
        .range([0, width - margin.left - margin.right])
        .padding(barPadding);
      var xScale1 = d3.scaleBand();
      var yScale = d3
        .scaleLinear()
        .range([height - margin.top - margin.bottom, 0]);

      formatValue = d3.format("~s");

      var xAxis = d3.axisBottom(xScale0).tickSizeOuter(axisTicks.outerSize);
      var yAxis = d3
        .axisLeft(yScale)
        .ticks(9)
        .tickFormat(function (d) {
          return formatValue(d).replace("G", " B$");
        });
      // .ticks(axisTicks.qty)
      // .tickSizeOuter(axisTicks.outerSize);

      xScale0.domain(models.map((d) => d.year));
      xScale1.domain(["budget", "revenue"]).range([0, xScale0.bandwidth()]);
      yScale.domain([
        0,
        d3.max(models, (d) => (d.budget > d.revenue ? d.budget : d.revenue)),
      ]);

      var model_name = svg
        .selectAll(".year")
        .data(models)
        .enter()
        .append("g")
        .attr("class", "year")
        .attr("transform", (d) => `translate(${xScale0(d.year)},0)`);

      /* Add field1 bars */
      model_name
        .selectAll(".bar.budget")
        .data((d) => [d])
        .enter()
        .append("rect")
        .attr("class", "bar budget")
        .style("fill", "grey")
        .attr("x", (d) => xScale1("budget"))
        .attr("y", (d) => yScale(d.budget))
        .attr("width", xScale1.bandwidth())
        .attr("height", (d) => {
          return height - margin.top - margin.bottom - yScale(d.budget);
        });

      /* Add field2 bars */
      model_name
        .selectAll(".bar.revenue")
        .data((d) => [d])
        .enter()
        .append("rect")
        .attr("class", "bar revenue")
        .style("fill", "orange")
        .attr("x", (d) => xScale1("revenue"))
        .attr("y", (d) => yScale(d.revenue))
        .attr("width", xScale1.bandwidth())
        .attr("height", (d) => {
          return height - margin.top - margin.bottom - yScale(d.revenue);
        });

      // Add the X Axis
      svg
        .append("g")
        .attr("class", "x axis")
        .attr(
          "transform",
          `translate(0,${height - margin.top - margin.bottom})`
        )
        .call(xAxis);

      // Add the Y Axis
      svg.append("g").attr("class", "y axis").call(yAxis);

      legend = (svg) => {
        const g = svg
          .attr("transform", `translate(${width},0)`)
          .attr("text-anchor", "end")
          .attr("font-family", "sans-serif")
          .attr("font-size", 100)
          .selectAll("g")
          .data(color.domain().slice().reverse())
          .join("g")
          .attr("transform", (d, i) => `translate(0,${i * 20})`);

        g.append("rect")
          .attr("x", -19)
          .attr("width", 19)
          .attr("height", 19)
          .attr("fill", color);

        g.append("text")
          .attr("x", -24)
          .attr("y", 9.5)
          .attr("dy", "0.35em")
          .text((d) => d);
      };
    }
  };
  xhttp.open("GET", "http://localhost:5000/aggregateMoviesBR", true);
  xhttp.send();
}
