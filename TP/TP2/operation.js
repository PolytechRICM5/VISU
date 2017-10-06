function readFile(e)
{

	var file = e.target.files[0];
  if (!file)
	{
    return;
  }

	var reader = new FileReader();
	reader.onload = function(e)
	{

		var data = e.target.result.split("\n");

    for (var i = 0; i < data.length; i++) {
      data[i] = data[i].split(" ");
    }

    main(data);

  };

  reader.readAsText(file);

}

function draw(data)
{
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  ctx.beginPath();
  ctx.moveTo(data[0][0], data[0][1]);
  for (var i in data) {
    ctx.lineTo(data[i][0], data[i][1]);
    ctx.moveTo(data[i][0], data[i][1]);
  }
  ctx.closePath();
  ctx.stroke();
}

function scale(data)
{

  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  var width = ctx.canvas.width;
  var height = ctx.canvas.height;

  for (i in data)
  {
    data[i][0] = data[i][0] * 30;
    data[i][1] = data[i][1] * 30;
  }

  return data

}

function main(data)
{
  data = scale(data);
  draw(data);
}

data = [];
data[0] = [0,0];
data[1] = [20,30];
data[2] = [30,50];

draw(data);
document.getElementById('file').addEventListener('change', readFile, false);
