//Select test subject ID no. and assign to a dropdown
var inputSelect = d3.select("#predict");

var outputSelect = d3.select("#output");

//var qtyBoxSelect = d3.select("#product-qty");

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// Create default display panel which updates when new value is selected

//inputSelect.on("change", optionChanged);
//
//  function optionChanged () {
//  
//  // Select number value from dropdown
//  var output_value = outputSelect.property('value');
//
//  if (output_value < 1) {
//    output_value = "Predicted Review Score: Negative";
//  } else {
//    output_value = "Predicted Review Score: Positive";
//  }
//
//  //Clear existing values in panel
//  //addList.html("");
//
//  var name_select = outputSelect.append("div");
//
//  var name_select = outputSelect.append("h2");
//  name_select.text(`${output_value}`);
//
//};

//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////


// Create default display panel which updates when new value is selected

inputSelect.on("change", optionChanged);

  function optionChanged () {
  
  // Select number value from dropdown
  var output_value = outputSelect.property('value');

  if (output_value < 1) {
    outputSelect = "Predicted Review Score: Negative";
  } else {
    output_value = "Predicted Review Score: Positive";
  }

  //Clear existing values in panel
  //addList.html("");

  var name_select = outputSelect.append("div");

  var name_select = outputSelect.append("ul");
  name_select.text(`${output_value}`);

};