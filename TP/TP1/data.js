// Lit une suite d'entiers dans un fichier.
// non utilisé actuellement.
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

		var len = data.length-1;
		var pow2len = Math.pow( 2, Math.round( Math.log( len ) / Math.log( 2 ) ) );

		var exp_data = []

		for(var i = 0; i < len; i++)
		{
			exp_data[i] = parseInt(data[i], 10);
		}

		for(var i = len; i < pow2len; i++)
		{
			exp_data[i] = 0;
		}

		console.log(exp_data);
		main(exp_data, 2);
  };

  reader.readAsText(file);

}

/**
  Crée le tableau contenant les valeurs correspondant à la fonction fun
  Dans l'intervalle [0,range] contenant exactement len valeurs.
*/
function funToArray(fun, range, len)
{

	var pow2len = Math.pow( 2, Math.round( Math.log( len ) / Math.log( 2 ) ) );
	var tab = [];

	for (var i = 0; i < len; i++) {
		tab[i] = fun(i/(len/range));
	}

	for (var i = len; i < pow2len; i++) {
		tab[i] = 0;
	}

	return tab;

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

/**
	Mets à 0 les valeurs de data inférieures au seuil donné
*/
function AppliquerSeuil(data,seuil)
{
	for(var i = 1; i < data.length; i++)
	{
		if(Math.abs(data[i]) <= seuil) data[i] = 0;
	}
	return data;
}

/**
  Calcule l'erreur totale entre les deux tableaux donnés en entrée
  Ceux ci doivent être de même taille !
*/
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


function AppliquerCompression(data,seuil){
	return RecompositionTotale(
			AppliquerSeuil(
				DecompositionTotale(data),
				seuil
			)
		);
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
		var compressed = AppliquerCompression(data,i);
		erreurs = erreurs.concat([CalculErreur(data,compressed)]);
		axe = axe.concat([i]);
	}
	var trace = {
		x : axe,
	    y: erreurs,
	    type : 'scatter',
	    mode : 'lines'
	  };
	var final = [trace];
	Plotly.newPlot('err', final);
}

function MultipleRecompoSeuil(data,step,max_seuil){
	var compressed = [];
	var trace = [];
	for(var i = 0.0; i <=max_seuil; i = i + step){
		compressed[i] = AppliquerCompression(data, i);
	}
	for(var i = 0.0; i <= max_seuil; i = i + step) {
		trace.push( {
			y: compressed[i],
			type : 'scatter',
			mode : 'lines'
		});
	}
	console.log(trace);
	Plotly.newPlot('multi', trace);
}

document.getElementById('file').addEventListener('change', readFile, false);

/*
document.getElementById('funToUse').addEventListener('change', function() {
	data = funToArray(document.getElementById('funToUse').value, document.getElementById('range').value);
	main(data, document.getElementById('seuil').value);
});
*/

function AppliquerValeurAbsolue(data,debut)
{
	var res = [];
	for(var i = debut; i < data.length; i++)
	{
		res[i] = Math.abs(data[i]);
	}
	return res;
}

function AfficherHistogrammeCoeffDetail(data){
	HISTO = document.getElementById('histo');
	var trace = {
	    x: AppliquerValeurAbsolue(data,1).slice(1),
	    type: 'histogram',
	  };
	var final = [trace];
	Plotly.newPlot(HISTO, final);
}

function AfficherDonnees(data,zone){
	var trace = {
	    y: data,
	    type : 'scatter'
	  };
	var final = [trace];
	Plotly.newPlot(zone, final);
}

function AfficherDeuxDonnees(data1, data2, zone){
	var trace1 = {
	    y: data1,
	    type : 'scatter',
	    mode : 'lines'
	  };
	var trace2 = {
	    y: data2,
	    type : 'scatter',
	    mode : 'lines'
	  };
	var final = [trace1,trace2];
	Plotly.newPlot(zone, final);
}

function main(donnees, seuil)
{
	var compressed = AppliquerCompression(donnees,seuil);
	/*var res = DecompositionTotale(donnees);
	console.log(donnees);
	console.log(compressed);
	console.log(CalculErreur(donnees,compressed));*/

	CalculErreurs(donnees,0.01,1);
	MultipleRecompoSeuil(donnees,0.2,1);
	AfficherHistogrammeCoeffDetail(compressed);
	AfficherDeuxDonnees(donnees,compressed,'data');
	
}

// génére un tableu contenant un sinus
data = funToArray(Math.sin, 2*Math.PI, 128);
// Appelle le main avec un  seuil de 0.1
main(data, 0.1);
