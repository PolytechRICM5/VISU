
function draw(data)
{
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  ctx.moveTo(data[0][0], data[0][1]);
  for (var point in data) {
    ctx.lineTo(point[0], point[1]);
    ctx.stroke();
  }
}


data = [];
data[0] = [0,0];
data[1] = [20,30];
data[2] = [30,50];

draw(data);
