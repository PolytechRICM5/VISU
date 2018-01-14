from __future__ import print_function
from paraview.simple import *
import vtk
import sys
import math

from MoteurContourConnecte import *


# DEBUT DU PROGRAMME PRINCIPAL

# LECTURE DU FICHIER METEO FRANCE AU FORMAT NETCDF
FichierNCComplet = NetCDFReader(FileName=sys.argv[1])
# fichierPourTestnc = NetCDFReader(FileName="../DATA/FichierPourTest.nc")
FichierNCComplet.Dimensions = '(latitude, longitude)'
FichierNCComplet.ReplaceFillValueWithNan = 1
FichierNCComplet.SphericalCoordinates = 0
FichierNCComplet.OutputType = 'Image'

# SELECTION DE L UNIQUE CHAMP TEMPERATURE
FichierNCTemperature = PassArrays(Input=FichierNCComplet)
FichierNCTemperature.PointDataArrays = ['TMP_2maboveground']


# SOUS-ECHANTILLONAGE RADICAL POUR AVOIR DES LIGNES DE CONTOUR SIMPLES
DonneesSousEchantillonnees = ExtractSubset(Input=FichierNCTemperature)
DonneesSousEchantillonnees.VOI = [0, 2800, 0, 1790, 0, 0]
#DonneesSousEchantillonnees.SampleRateI = 1
#DonneesSousEchantillonnees.SampleRateJ = 1
DonneesSousEchantillonnees.SampleRateI = 50
DonneesSousEchantillonnees.SampleRateJ = 50

# NE SELECTIONNE QUE LA PARTIE DU DOMAINE OU LES DONNEES SONT DEFINIES, EN SUPPRIMANT TOUTES LES DONNEES NAN
DonneesValides = Threshold(Input=DonneesSousEchantillonnees)
DonneesValides.Scalars = ['POINTS', 'TMP_2maboveground']
DonneesValides.ThresholdRange = [0., 500.]

# CONVERTIT AU FORMAT SURFACE ...
FormatSurface = ExtractSurface(Input=DonneesValides)

# ... PUIS AU FORMAT TRIANGLE ...
FormatTriangle = Triangulate(Input=FormatSurface)

# ... POUR POUVOIR APPLIQUER UNE SUBDIVISION DE LOOP, QUI AURA POUR EFFET D'OBTENIR DES CONTOUR LISSES (EN PLUS D ETRE SIMPLES)
DonneesSubdivisees = LoopSubdivision(Input=FormatTriangle)
DonneesSubdivisees.NumberofSubdivisions = 5
#DonneesSubdivisees.NumberofSubdivisions = 0

# PREPARATION DU FILTRE CONTOUR
CourbesDeContour = Contour(Input=DonneesSubdivisees)
CourbesDeContour.ContourBy = ['POINTS', 'TMP_2maboveground']
# contourTemperature.Isosurfaces = [10. + 273.15] # Contour de temperature a 10 degres celsius
CourbesDeContour.PointMergeMethod = 'Uniform Binning'

print("<kml>")
print("<Document>")
print("<name>ICILENOM</name>")
print("<description>ICILENOM</description>")
print("<TimeStamp>")
print("  <when> ICILADATEDELAPREVISION </when>")
print("</TimeStamp>")


# BOUCLE SUR LES TEMPERATURES
#MesTemperatures=[15.]
#MesCouleurs=["ff0aa0fa"]
MesTemperatures=[0., 3., 5., 7., 10., 11., 13., 15., 17., 20., 25.]
MesCouleurs=["ffff0080","ffff8010","ffff8020", "ffa06010", "ff258010", "ff109080", "ff0fe0f2", "ff0aa0fa", "ff0a66f9", "ff0a36f9", "ff0000ff"]
#MesTemperatures=[0.]
#MesCouleurs=["ff000000"]

for i in range(len(MesCouleurs)):
	print("<Style id=\"ContourValeurId" +str(i)+"\">")
	print("	<LineStyle>")
	print("	<width> 3 </width>")
	print("	<color>"+MesCouleurs[i]+"</color>")
	print("	</LineStyle>")
	print("</Style>")

nT = 0
for Temperature in MesTemperatures:
	CourbesDeContour.Isosurfaces = [Temperature + 273.15] # CHANGEMENT DE LA VALEUR DE CONTOUR

# CALCUL DE LA CONNECTIVITE DU CONTOUR
# ExtractionMode=4 => ON EXTRAIT UNIQUEMENT LE PLUS GRAND CONTOUR
	MonContourConnecte = Connectivity(Input=CourbesDeContour,ExtractionMode=5)
# MonContourConnecte = Connectivity(Input=contourTemperature)

# ACTIVATION DU CALCUL PARAVIEW
	MonContourConnecte.UpdatePipeline()

# RECUPERATION DES DONNEES CALCULEES
	MesDonneesDuContour=servermanager.Fetch(MonContourConnecte)

# APPEL DE LA PROCEDURE DE CONVERSION DES CONTOURS DEFINIE AU DEBUT DE CE CODE SOURCE
	ConvertitDonneesContourEnKML( MesDonneesDuContour, str(Temperature)+" degres celsius", nT)
	nT = nT+1

print("</Document>")
print("</kml>")

