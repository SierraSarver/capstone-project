$(".main").hide();

$("#remind-me-later").click(function() {
  $(".check-in").fadeOut();
  $(".main").fadeIn();
});

var slider = document.getElementById("mood-score");
var output = document.getElementById("value");

slider.oninput = function () {
  output.innerHTML = this.value;
}

$("#add-mood").click(function() {
  $(".check-in").fadeOut();
  $(".main").fadeIn();
});
