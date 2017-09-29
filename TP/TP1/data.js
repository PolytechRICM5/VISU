

function readTextFile(file)
{
	var file = evt.target.file; // Recupère le fichier listé par l'event
	var reader = new FileReader();

    var fs = require("fs"); // Récupère la librairie fs et la stocke dans la variable fs
	var text = fs.readFileSync(file);
	var textByLine = text.split("\n")/*.map(parseFloat());*/;
	alert(textByLine);
}

function EtapeDecomposition(data,taille)
{
	var x = [];
	var y = [];
	for( var i = 0; i < taille/2; i++)
	{
		x[i] = (data[2*i] + data[(2*i)+1])/2;
		y[i] = (data[2*i] - data[(2*i)+1])/2
	}
	return x.concat(y);
}

function DecompositionTotale(data)
{
	var taille = data.length;
	for(var i = taille; i > 1; i = i/2)
	{
		var res = EtapeDecomposition(data,i);
		data = res.concat(data.slice(i));
	}
	return data;
}

function EtapeRecomposition(data,taille)
{
	var res = [];
	var sous_taille = taille/2
	for(var i = 0; i < sous_taille; i++)
	{
		res[2*i] = data[i] + data[sous_taille+i];
		res[2*i+1] = data[i] - data[sous_taille+i];
	}
	return res;
}

function RecompositionTotale(data)
{
	var taille = data.length;
	for(var i = 2; i <= taille; i = i*2)
	{
		var res = EtapeRecomposition(data, i);
		data = res.concat(data.slice(i));
	}
	return data;
}

function AppliquerSeuil(data,seuil)
{
	for(var i = 1; i < data.length; i++)
	{
		if(Math.abs(data[i]) <= seuil) data[i] = 0;
	}
	return data;
}

function CalculErreur(data_o,data_r)
{
	var erreur = 0;
	var taille = data_o.length;
	for(var i = 0; i < taille; i++)
	{
		erreur = erreur + Math.pow(data_o[i] - data_r[i],2);
	}
	return erreur;
}

//readTextFile("./file.txt");
var donnees = [9,7,3,5];
//alert(EtapeDecomposition(donnees, 8));
var res = DecompositionTotale(donnees);
console.log(RecompositionTotale(res));
var compressed = AppliquerSeuil(res,1);
console.log(compressed);
var reco =RecompositionTotale(compressed);
console.log(reco);
console.log(CalculErreur(donnees,reco));

