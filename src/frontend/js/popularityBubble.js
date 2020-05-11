function popularityBubble() {
  
  chart = {
    const root = pack(data);
    
    const svg = d3.create("svg")
        .attr("viewBox", [0, 0, width, height])
        .attr("font-size", 10)
        .attr("font-family", "sans-serif")
        .attr("text-anchor", "middle");
  
    const leaf = svg.selectAll("g")
      .data(root.leaves())
      .join("g")
        .attr("transform", d => `translate(${d.x + 1},${d.y + 1})`);
  
    leaf.append("circle")
        .attr("id", d => (d.leafUid = DOM.uid("leaf")).id)
        .attr("r", d => d.r)
        .attr("fill-opacity", 0.7)
        .attr("fill", d => color(d.data.group));
  
    leaf.append("clipPath")
        .attr("id", d => (d.clipUid = DOM.uid("clip")).id)
      .append("use")
        .attr("xlink:href", d => d.leafUid.href);
  
    leaf.append("text")
        .attr("clip-path", d => d.clipUid)
      .selectAll("tspan")
      .data(d => d.data.name.split(/(?=[A-Z][a-z])|\s+/g))
      .join("tspan")
        .attr("x", 0)
        .attr("y", (d, i, nodes) => `${i - nodes.length / 2 + 0.8}em`)
        .text(d => d);
  
    leaf.append("title")
        .text(d => `${d.data.title === undefined ? "" : `${d.data.title}
  `}${format(d.value)}`);
      
    return svg.node();
  }
}
