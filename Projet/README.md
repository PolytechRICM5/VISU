#Projet simulation

## Discrétisation de 4 espaces avec un degré de précision différent
* Code "Arpage"
 * Globe > Cellules de précision 0.5° : 720*360
  * longitude `--` : -180 + 180° et latitude `|` : -90 +90°
  * Dessin sur le globe ou à plat
  * Arpage
 * Europe "Grande" > Sous-zone 0.1° de précision
  * ArpageHD
* Code "Arome"
 * Europe "Centrée" > Précision 0.025°
  * Arome
 * France > Précision 0.01° en lon et lat
  * AromeHD

## Dates utilisées
1. Date à laquelle la simulation a été effectuée
 * C'est la date du **RUN**
2. Date pour laquelle la prévision est faite
 * C'est la date de **Prévision**
 * Ex : à 3h du matin on a prévu la température pour 12h,
    à 6h du matin, on a prévu la température pour 12h également

Il faudra préciser ces informations pour la visualisation

## Contenus des fichiers
Fichier **RUN** de 3h du matin qui contient les précisions de 12h à 16h.

## Format des données météo France
> GRIB

-> Conversion au format NetCDF
Lisible par Paraview

## Paraview
* NetCDF open
* Spherical coordinates > Plat ou globe
* Replace fill values with NaN > oui
 * Dimenssion > height above ground ,lat, lon
=> Apply
* Sélectionner "température height above ground au lieu de solid color"
* Température en Kelvin, il va falloir adapter
 * Filtre Couteau suisse "Calculator"
  * Scalars : choix température - 273.15
  * Result name : TMP_Celsius
