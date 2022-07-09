// document.getElementById("e5").addEventListener("onclick", changeGraph;
// document.getElementById("syde-lounge").addEventListener("click", changeGraph);
// document.getElementById("dc-library").addEventListener("click", changeGraph);
// document.getElementById("all-locations").addEventListener("click", changeGraph);

document.getElementById('temp-all-locations').checked="true";
document.getElementById('hum-all-locations').checked="true";
document.getElementById('light-all-locations').checked="true";

function changeTempGraph() {

  if(document.getElementById('temp-e5').checked) {
  document.getElementById("temp-graph-img").src = "images/e5-classroom.jpg";
    }

  else if(document.getElementById('temp-syde-lounge').checked) {
  document.getElementById("temp-graph-img").src = "images/syde-lounge.jpg";
    }

  else if (document.getElementById('temp-dc-library').checked) {
  document.getElementById("temp-graph-img").src = "images/dc-library.jpg";
    }

  else if (document.getElementById('temp-all-locations').checked) {
  document.getElementById("temp-graph-img").src = "images/all-locations.jpg";
    }

};

function changeHumGraph() {

  if(document.getElementById('hum-e5').checked) {
  document.getElementById("hum-graph-img").src = "images/e5-classroom.jpg";
    }

  else if(document.getElementById('hum-syde-lounge').checked) {
  document.getElementById("hum-graph-img").src = "images/syde-lounge.jpg";
    }

  else if (document.getElementById('hum-dc-library').checked) {
  document.getElementById("hum-graph-img").src = "images/dc-library.jpg";
    }

  else if (document.getElementById('hum-all-locations').checked) {
  document.getElementById("hum-graph-img").src = "images/all-locations.jpg";
    }

};

function changeLightGraph() {

  if(document.getElementById('light-e5').checked) {
  document.getElementById("light-graph-img").src = "images/e5-classroom.jpg";
    }

  else if(document.getElementById('light-syde-lounge').checked) {
  document.getElementById("light-graph-img").src = "images/syde-lounge.jpg";
    }

  else if (document.getElementById('light-dc-library').checked) {
  document.getElementById("light-graph-img").src = "images/dc-library.jpg";
    }

  else if (document.getElementById('light-all-locations').checked) {
  document.getElementById("light-graph-img").src = "images/all-locations.jpg";
    }

};
