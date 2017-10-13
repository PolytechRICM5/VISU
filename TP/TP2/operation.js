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

function draw(data, nb_pts)
{

	var nb_pts = Math.min(nb_pts, data.length);

	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");
	ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
	ctx.beginPath();
	ctx.moveTo(data[0][0], data[0][1]);
	for (var i = 0; i < nb_pts; i++)
	{
		ctx.lineTo(data[i][0], data[i][1]);
	}
	ctx.lineTo(data[0][0], data[0][1]);
	ctx.closePath();
	ctx.stroke();
}

function rotate(data)
{

	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");

	for(var i = 0; i < data.length; i++)
	{
		data[i][0] = ctx.canvas.width - data[i][0];
		data[i][1] = ctx.canvas.height - data[i][1];
	}

	return data;

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
	data = rotate(data);
	console.log(data.length);
	data = EtapeDecomposition(data, data.length-1);
	draw(data, (data.length-1)/2);
}

data = [];
data[0] = [10,10];
data[1] = [100,30];
data[2] = [200,10];
data[3] = [180,100];
data[4] = [200,200];
data[5] = [100,180];
data[6] = [10,200];
data[7] = [30,100];

draw(data, data.length);
document.getElementById('file').addEventListener('change', readFile, false);



function EtapeDecomposition(data,taille){
	var x = [];
	var y = [];

	x[0] =[
	( - data[taille-2][0] + 3 * data[taille-1][0] + 3 * data[0][0] - data[1][0]) / 4,
	( - data[taille-2][1] + 3 * data[taille-1][1] + 3 * data[0][1] - data[1][1]) / 4
	];
	y[0] = [
	( data[taille-2][0] - 3 * data[taille-1][0] + 3 * data[0][0] - data[1][0]) / 4,
	( data[taille-2][1] - 3 * data[taille-1][1] + 3 * data[0][1] - data[1][1]) / 4
	];

	for( var i = 1; i < taille/2; i++)
	{
		x[i] = [
		( - data[2*i-2][0] + 3 * data[(2*i)-1][0] + 3 * data[2*i][0] - data[2*i+1][0]) / 4,
		( - data[2*i-2][1] + 3 * data[(2*i)-1][1] + 3 * data[2*i][1] - data[2*i+1][1]) / 4
		];
		y[i] = [
		( data[2*i-2][0] - 3 * data[(2*i)-1][0] + 3 * data[2*i][0] - data[2*i+1][0]) / 4,
		( data[2*i-2][1] - 3 * data[(2*i)-1][1] + 3 * data[2*i][1] - data[2*i+1][1]) / 4
		];
	}
/*
	x[max][0] = ( - data[2*i-2][0] + 3 * data[(2*i)-1][0] + 3 * data[2*i][0] - data[2*i+1][0]) / 4;
	x[max][1] = ( - data[2*i-2][1] + 3 * data[(2*i)-1][1] + 3 * data[2*i][1] - data[2*i+1][1]) / 4;
	y[max][0] = ( data[2*i-2][0] - 3 * data[(2*i)-1][0] + 3 * data[2*i][0] - data[2*i+1][0]) / 4;
	y[max][1] = ( data[2*i-2][1] - 3 * data[(2*i)-1][1] + 3 * data[2*i][1] - data[2*i+1][1]) / 4;
	*/
	return x.concat(y);
}

function DesEtapesDecomposition(data, steps){
	var res = data;
	var size = data.length;
	for(var i = 0; i < steps; i++) {
		res = EtapeDecomposition(res,size);
		size = size/2;
	}
	return [res,size];
}

function EtapeRecomposition(data, taille){
	var x = [];
	var size = taille/2;
	for( var i = 0; i < size - 1 ; i++)
	{
		x[2*i] = [
		3 * ( data[i][0] + data[size+i][0]) / 4 + (data[i+1][0] - data[size+i+1][0]) / 4,
		3 * ( data[i][1] + data[size+i][1]) / 4 + (data[i+1][1] - data[size+i+1][1]) / 4
		];
		x[2*i+1] = [
		( data[i][0] + data[size+i][0]) / 4 + 3 * (data[i+1][0] - data[size+i+1][0]) / 4,
		( data[i][1] + data[size+i][1]) / 4 + 3 * (data[i+1][1] - data[size+i+1][1]) / 4
		];
	}
	x[taille-2] = [
	3 * ( data[size-1][0] + data[taille-1][0]) / 4 + (data[0][0] - data[size][0]) / 4,
	3 * ( data[size-1][1] + data[taille-1][1]) / 4 + (data[0][1] - data[size][1]) / 4
	];
	x[taille-1] = [
	( data[size-1][0] + data[taille-1][0]) / 4 + 3 * (data[0][0] - data[size][0]) / 4,
	( data[size-1][1] + data[taille-1][1]) / 4 + 3 * (data[0][1] - data[size][1]) / 4
	];
	return x;
}

