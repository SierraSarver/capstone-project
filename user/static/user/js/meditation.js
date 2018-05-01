// Meditation Static JavaScript

var time = setInterval(myfunction,4000);
var time = 0

function myfunction(){
  time++;
  if(time % 2 == 0){
  document.getElementById("demo").innerHTML = "Breathe In"
  }
  else{
  document.getElementById("demo").innerHTML = "Breathe Out"
  }
}
