#!/bin/bash
if [ "$#" -eq 0 ]; then
        echo "vous devez donnez le nombre d'heure a partir du moment actuel pour lequel vous voulez la prevision"
	echo
	exit
else
        echo "== TELECHARGEMENT ET VISUALISATION DES DONNEES DE SIMULATION METEOFRANCE POUR DANS $1 HEURE(S)"
fi

echo "=== TELECHARGEMENT DES DONNEES DE SIMULATION A METEOFRANCE"
echo

NomDuFichierMeteoFrance=`python PYTHON/RequeteAromeHD.py $1 SP1`
rc=$?
if ! [ $rc == 0 ]; then
	echo "LES DONNEES N ONT PAS PU ETRE TELECHARGEE A METEOFRANCE"
	exit 1
fi

DateDeLaPrevision=`python PYTHON/DateDeLaPrevisionAromeHD.py $1`
DateDuRun=`python PYTHON/DateDuRunAromeHD.py $1`
if [ -e  $NomDuFichierMeteoFrance ]; then
	mv $NomDuFichierMeteoFrance DATA
fi

if ! [ -e DATA/$NomDuFichierMeteoFrance ]; then
	echo "LE CHARGEMENT DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUE"
	exit 1
fi

echo "LES DONNEES DE SIMULATION SONT SAUVEES DANS LE FICHIER DATA/$NomDuFichierMeteoFrance"
echo

echo "=== CONVERSION EN NC DES DONNEES METEOFRANCE, EN NE CONSERVANT QUE LA TEMPERATURE"
echo

if [ -e DATA/$NomDuFichierMeteoFrance.nc ]; then
	echo "LE FICHIER NC EXISTE DEJA"
else
	wgrib2 DATA/$NomDuFichierMeteoFrance -match ":TMP:" -netcdf DATA/$NomDuFichierMeteoFrance.nc
	rc=$?
	if ! [ $rc == 0 ]; then
		echo "LES DONNEES TELECHARGEES AU FORMAT GRIB2 N ONT PAS PU ETRE CONVERTIES AU FORMAT NC"
		exit 1
	fi
fi

if ! [ -e DATA/$NomDuFichierMeteoFrance.nc ]; then
	echo "LES DONNEES TELECHARGEES AU FORMAT GRIB2 N ONT PAS PU ETRE CONVERTIES AU FORMAT NC"
	exit 1
fi


echo "LES DONNEES PARAVIEW SONT SAUVEES DANS LE FICHIER DATA/$NomDuFichierMeteoFrance.nc"
echo

echo "=== CREATION DU FICHIER KML PAR PARAVIEW ET PYTHON"
echo

if [ -e KML/$NomDuFichierMeteoFrance.contour.kml ]; then
	echo "LES CONTOURS SONT DEJA SAUVES DANS UN KML"
else
	pvpython PYTHON/ContourConnecteEnKML.py DATA/$NomDuFichierMeteoFrance.nc > tmp.kml
	rc=$?
	if ! [ $rc == 0 ]; then
		echo "LES CONTOURS N ONT PAS PU ETRE CALCULES PAR PARAVIEW"
		exit 1
	fi
	cat tmp.kml | sed "s/ICILENOM/RUN_DU_$DateDeLaPrevision/g" > tmp1.kml
	cat tmp1.kml | sed "s/ICILADATEDELAPREVISION/$DateDeLaPrevision/g" > KML/$NomDuFichierMeteoFrance.contour.kml
	rm tmp.kml tmp1.kml
	cd KML; zip $NomDuFichierMeteoFrance.contour.kmz $NomDuFichierMeteoFrance.contour.kml; cd ..
#	rm KML/$NomDuFichierMeteoFrance.contour.kml
fi

echo "LE FICHIER KMZ KML/$NomDuFichierMeteoFrance.contour.kmz PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo

#=================================================================================
# TELEVERSEMENT DU FICHIER SUR LE REPERTOIRE KML DE GOOGLE DRIVE
# IdDuRepertoireGoogleDrive=IndiquerICILaCleDuRepertoireSurGoogleDrive
# gdrive upload --parent $IdDuRepertoireGoogleDrive KML/$NomDuFichierMeteoFrance.contour.kml
echo "SI VOUS VOULEZ TELEVERSER VOS VISUALISATIONS SUR UN REPERTOIRE GOOGLE DRIVE, MODIFIEZ LE SCRIPT RUNME_CONTOUR.sh"

rc=$?
if ! [ $rc == 0 ]; then
	echo "LES CONTOURS N ONT PAS PU ETRE TELEVERSES SUR GOOGLE DRIVE"
	exit 1
fi

exit 0

