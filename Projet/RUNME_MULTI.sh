#!/bin/bash
if [ "$#" -ne 2 ] && ["$1" -lt "$2" ]; then
        echo "vous devez donnez une plage horaire a partir du moment actuel pour lequel vous voulez la prevision"
	echo
	exit
else
        # ==================================================================================================
        echo "=== CREATION DU FICHIER KML POUR GOOGLE EARTH"
        echo
        
        cat KML/templateKMZ_TOP.kml | sed "s/ICILEFICHIER/$NomDuFichierMeteoFrance.nc.png/g" | sed "s/ICILENOM/RUN_DU_$DateDuRun/g" > tmp.kml

        echo "== TELECHARGEMENT ET VISUALISATION DES DONNEES DE SIMULATION METEOFRANCE ENTRE DANS $1 HEURE(S) et $2 HEURE(S)"
fi

for ((i=$1; i<=$2; i++));
do
        # ==================================================================================================
        echo "=== TELECHARGEMENT DES DONNEES DE SIMULATION A METEOFRANCE"
        echo

        NomDuFichierMeteoFrance=`python PYTHON/RequeteAromeHD.py $i SP1`
        rc=$?
        if ! [ $rc == 0 ]; then
	        echo "LE CHARGEMENT DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUE"
	        exit 1
        fi

        DateDeLaPrevision=`python PYTHON/DateDeLaPrevisionAromeHD.py $i`
        DateDuRun=`python PYTHON/DateDuRunAromeHD.py $i`
        if [ -e  $NomDuFichierMeteoFrance ]; then
	        mv $NomDuFichierMeteoFrance DATA
        fi

        if ! [ -e DATA/$NomDuFichierMeteoFrance ]; then
	        echo "LE CHARGEMENT DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUE"
	        exit 1
        fi

        echo "LES DONNEES DE SIMULATION SONT SAUVEES DANS LE FICHIER DATA/$NomDuFichierMeteoFrance"
        echo

        # ==================================================================================================
        echo "=== CONVERSION EN NC DES DONNEES METEOFRANCE"
        echo

        if [ -e DATA/$NomDuFichierMeteoFrance.nc ]; then
	        echo "LE FICHIER NC EXISTE DEJA"
        else
	        wgrib2 DATA/$NomDuFichierMeteoFrance -netcdf DATA/$NomDuFichierMeteoFrance.nc
                #-match ":TMP:"
	        rc=$?
        fi

        if ! [ $rc == 0 ]; then
	        echo "LA CONVERSION DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUEE"
	        exit 1
        fi

        if ! [ -e DATA/$NomDuFichierMeteoFrance.nc ]; then
	        echo "LA CONVERSION DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUEE"
	        exit 1
        fi


        echo "LES DONNEES PARAVIEW SONT SAUVEES DANS LE FICHIER DATA/$NomDuFichierMeteoFrance.nc"
        echo
        
        # ==================================================================================================
        echo "=== CREATION DE L IMAGE PNG PAR PARAVIEW"
        echo

        if [ -e KML/IMAGES/$NomDuFichierMeteoFrance.nc.png ]; then
	        echo "L IMAGE EXISTE DEJA"
        else
	        #pvpython PYTHON/VisuAvecTemperature.py DATA/$NomDuFichierMeteoFrance.nc
          pvpython PYTHON/FirstPipeline.py DATA/$NomDuFichierMeteoFrance.nc
        #	pvpython PYTHON/VisuAvecVentEtTemperature.py DATA/$NomDuFichierMeteoFrance.nc
        #	pvpython PYTHON/VisuAvecVentSeulement.py DATA/$NomDuFichierMeteoFrance.nc
	        rc=$?

	        if ! [ $rc == 0 ]; then
		        echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		        exit 1
	        fi

	        if ! [ -e DATA/$NomDuFichierMeteoFrance.nc.png ]; then
		        echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		        exit 1
	        fi
	        mv DATA/$NomDuFichierMeteoFrance.nc.png KML/IMAGES
	        convert -trim -define png:color-type=6 KML/IMAGES/$NomDuFichierMeteoFrance.nc.png KML/IMAGES/$NomDuFichierMeteoFrance.nc.png
	        if ! [ $rc == 0 ]; then
		        echo "L IMAGE N A PAS PU ETRE TRAITEE PAR IMAGEMAGICK"
		        exit 1
	        fi
        fi

        echo "L IMAGE EST SAUVEE DANS LE FICHIER KML/IMAGES/$NomDuFichierMeteoFrance.nc.png"
        echo

done

exit 0


cat KML/templateKMZ.kml | sed "s/ICILEFICHIER/$NomDuFichierMeteoFrance.nc.png/g" > tmp.kml
cat tmp.kml | sed "s/ICILENOM/RUN_DU_$DateDuRun/g" > tmp1.kml
cat tmp1.kml | sed "s/ICILADATEDELAPREVISION/$DateDeLaPrevision/g" > KML/$NomDuFichierMeteoFrance.nc.png.kml
rm tmp.kml tmp1.kml

echo "LE FICHIER KML KML/$NomDuFichierMeteoFrance.nc.png.kml PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo

# ==================================================================================================
echo "=== CREATION DE L ARCHIVE KMZ POUR GOOGLE EARTH"
echo

cd KML; zip $NomDuFichierMeteoFrance.nc.png.kmz IMAGES/$NomDuFichierMeteoFrance.nc.png $NomDuFichierMeteoFrance.nc.png.kml


echo "LE FICHIER KMZ KML/$NomDuFichierMeteoFrance.nc.png.kmz PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo
