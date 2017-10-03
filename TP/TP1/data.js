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
		var total_len = Math.pow(2,Math.ceil(Math.sqrt(len)));

		var exp_data = []

		for(var i = 0; i < len; i++)
		{
			exp_data[i] = parseInt(data[i], 10);
		}

		for(var i = len; i < total_len; i++)
		{
			exp_data[i] = 0;
		}

		console.log(exp_data);
		main(exp_data);
  };

  reader.readAsText(file);

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

function main(donnees)
{
	var res = DecompositionTotale(donnees);
	var seuil = AppliquerSeuil(res,1);
	var compressed =RecompositionTotale(seuil);
	console.log(CalculErreur(donnees,compressed));
	
	AfficherHistogrammeCoeffDetail(compressed);
	AfficherDeuxDonnees(donnees,compressed,'data');

}

document.getElementById('file').addEventListener('change', readFile, false);

//readTextFile("./file.txt");
var donnees = [9,7,3,5];

function AppliquerValeurAbsolue(data,debut)
{
	for(var i = debut; i < data.length; i++)
	{
		data[i] = Math.abs(data[i]);
	}
	return data;
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

/*Plotly.plot( HISTO, [{
	y : res.slice(1) }], {
	margin: { t: 0 } } );*/
