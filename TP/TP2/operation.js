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
		data.splice(-1);
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

function drawc(data, nb_pts, canvas)
{
    var nb_pts = Math.min(nb_pts, data.length);
    var canvas = document.getElementById(canvas);
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
		data[i][0] = data[i][0] * 20;
		data[i][1] = data[i][1] * 20;
	}

	return data
}

function translate(data)
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    var width = ctx.canvas.width;
    var height = ctx.canvas.height;

    for (i in data)
    {
        data[i][0] = data[i][0] + 50;
        data[i][1] = data[i][1] + 50;
    }

    return data
}

function norme(point)
{
	return Math.sqrt(Math.pow(point[0],2) + Math.pow(point[1], 2));
}

function distance(point1,point2) {
	return Math.sqrt( Math.pow((point1[0]-point2[0]),2) + Math.pow((point1[1]-point2[1]),2));
}

function seuil(data, seuil)
{
	var data2 = data;
	for (var i = 3; i < data2.length; i++)
	{
		if(Math.sqrt(Math.pow(data2[i][0],2) + Math.pow(data2[i][1], 2)) <= seuil)
		{
			data2[i][0] = 0.0;
			data2[i][1] = 0.0;
		}
	}
	return data2;
}

function main(data)
{
	data = scale(data);
	data = translate(data);
	data = rotate(data);
	[res,size] = DecompositionTotale(data);
	//var data2 = seuil(res,10);
	var res2 = res.slice();
	console.log(res2);
	res2[3] = [150, 100];
	data3 = RecompositionTotale(res2,size*2);
	draw(data,data.length);
  	drawc(res,size,"canvas2");
    drawc(res2,size,"canvas3");
    drawc(data3,data3.length,"canvas4");
  	CalculErreurs(data,1,200);
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
	var base = data;
	var size = data.length;
	for(var i = 0; i < steps; i++) {
		if(size <= 2) break;
		var res = EtapeDecomposition(base,size);
		base = res.concat(base.slice(size));
		size = size/2;
	}
	return [base,size];
}

function DecompositionTotale(data){
	var base = data;
	for(var i = data.length; i > 4; i = i / 2) {
		var res = EtapeDecomposition(base,i);
        base = res.concat(base.slice(i));
	}
	return [base,i];
}

/*
@taille : la taille des donnée + le détail à prendre en compte.
 */
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

/*
@start : la taille des points constituant la figure décomposée (en général 4 points)
		+ les coefficients de détail associés
 */
function RecompositionTotale(data, start) {
	var base = data;
	var taille = data.length;
	console.log(start);
	for(var i = start; i <= taille; i = i * 2){
		var res  = EtapeRecomposition(base,i);
		base = res.concat(base.slice(i));
	}
	return res;
}

function calculErreur(data, data_err)
{
	var erreur = 0;
	for (var i = 0; i < data.length; i++) {
		erreur += Math.pow(distance(data[i], data_err[i]), 2);
	}
	erreur /= data.length;
	return erreur;
}

/**
 Calcule les erreurs pour les seuils correspondant à
 tout les 'step' sur l'intervalle [0,len]
 et affiche la courbe des erreurs correpondante
 */
function CalculErreurs(data,step,len){
    var erreurs = [];
    var axe = [];
    for(var i = 0.0; i <=len; i = i + step){
        [decompose,taille] = DecompositionTotale(data);
        var seuille = seuil(decompose,i);
        var res = RecompositionTotale(seuille,taille*2);
        erreurs = erreurs.concat([calculErreur(data,res)]);
        axe = axe.concat([i]);
    }
    var trace = {
        x : axe,
        y : erreurs,
        type : 'scatter',
        mode : 'lines'
    };
    var final = [trace];
    Plotly.newPlot('erreur', final);
}