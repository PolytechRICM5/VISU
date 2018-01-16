from __future__ import print_function
from paraview.simple import *
import vtk
import sys
import math

def ParcoursDansUnSens(SegmentCourant, PointCourant, PointDeBouclage, TousLesSommetsDansLeBonSens, TousLesSegmentsValidesEtNonParcourus, MesDonneesDuContour):

	MesPoints=MesDonneesDuContour.GetPoints() # on accede aux points

	UneSeulePtId = vtk.vtkIdList()
	UneSeulePtId.InsertNextId(0) # on initialise une liste de un indice de sommet
	UneSeuleCellId = vtk.vtkIdList() # on initialise une liste d indices de cellules qui servira a determiner le segment suivant

	FinLigne = False

	while (not FinLigne) :

		TousLesSegmentsValidesEtNonParcourus.DeleteId( SegmentCourant) # ON SUPPRIME SegmentCourant DANS LA LISTE DES SEGMENTS NON PARCOURUS

#		sys.stderr.write("jai supprime le segment suivant dans la liste des segments parcourus: ")
#		sys.stderr.write(str(SegmentCourant))
#		sys.stderr.write("\n")

		TousLesSommetsDansLeBonSens.InsertNextId( PointCourant) # ON RAJOUTE PointCourant DANS LA LISTE DE SORTIE

		# ON INCREMENTE LE SEGMENT COURANT EN RECHERCHANT L UNIQUE AUTRE SEGMENT CONTENANT PointCourant
		UneSeulePtId.InsertId( 0, PointCourant)
		MesDonneesDuContour.GetCellNeighbors( SegmentCourant, UneSeulePtId, UneSeuleCellId)
		# ON DOIT AVOIR UneSeuleCellId.GetNumberOfIds() == 1
		FinLigne =  (UneSeuleCellId.GetNumberOfIds() != 1)
		if (not FinLigne):
			SegmentCourant = UneSeuleCellId.GetId(0)

			Cell = MesDonneesDuContour.GetCell(SegmentCourant)
			PtIds = Cell.GetPointIds() # on accede aux indices des sommets du segment courant

			# on modifie PointCourant en "avancant le long du segment"
			if (PtIds.GetId(0) == PointCourant):
				PointCourant = PtIds.GetId(1)
			else:
				PointCourant = PtIds.GetId(0)

			CoordonneesPoint = MesPoints.GetPoint(PointCourant)

			FinLigne = math.isnan(CoordonneesPoint[0]) | math.isnan(CoordonneesPoint[1]) | math.isnan(CoordonneesPoint[2])
			FinLigne = FinLigne | (PointCourant == PointDeBouclage)

	if (PointCourant == PointDeBouclage):
		TousLesSommetsDansLeBonSens.InsertNextId( PointCourant)

	TousLesSegmentsValidesEtNonParcourus.DeleteId( SegmentCourant)

#	sys.stderr.write("jai supprime le segment suivant dans la liste des segments parcourus: ")
#	sys.stderr.write(str(SegmentCourant))
#	sys.stderr.write("\n")

	return PointCourant

# FIN DE ParcoursDansUnSens

def EcritUneLigneEnKML( TousLesSommetsDansLeBonSens, MesDonneesDuContour, Nom, IndiceCouleurDuContour):

	MesPoints=MesDonneesDuContour.GetPoints() # on accede aux points

	print("<Placemark>")
	print("<name> " + Nom + " </name>")
	print("<TimeSpan>")
	print("  <when> ICILADATEDELAPREVISION </when>")
	print("</TimeSpan>")
	print("<styleUrl>#ContourValeurId"+str(IndiceCouleurDuContour)+"</styleUrl>")
	print("<LineString>")
	print("<coordinates>")

	for i in range(0,TousLesSommetsDansLeBonSens.GetNumberOfIds()):
		PointId = TousLesSommetsDansLeBonSens.GetId(i)
		Point = MesPoints.GetPoint(PointId)
		print(Point[0], end="")
		print(",", end="")
		print(Point[1], end="")
		print(",", end="")
		print(Point[2])

	print("</coordinates>")
	print("</LineString>")
	print("</Placemark>")
# FIN DE ConvertitUneDemiLigneEnKML

def InitialiseLesSegmentsSansNanEtNonParcourus( TousLesSegmentsValides, MesDonneesDuContour):

	MesPoints=MesDonneesDuContour.GetPoints() # on accede aux points

	# RECHERCHE DE TOUS LES SEGMENTS NE CONTENANT AUCUN SOMMET NAN

	SegmentValide = False
	SegmentCourant = -1

	while (SegmentCourant+1 < MesDonneesDuContour.GetNumberOfCells()):

		SegmentCourant = SegmentCourant+1

		Cell = MesDonneesDuContour.GetCell(SegmentCourant)
		PtIds = Cell.GetPointIds()

		PointDeBouclage = PtIds.GetId(0);
		PointCourant = PtIds.GetId(1);

		CP1 = MesPoints.GetPoint(PointDeBouclage)
		CP2 = MesPoints.GetPoint(PointCourant)
		SegmentValide = True
		SegmentValide = SegmentValide & (not math.isnan(CP1[0]))
		SegmentValide = SegmentValide & (not math.isnan(CP1[1]))
		SegmentValide = SegmentValide & (not math.isnan(CP1[2]))
		SegmentValide = SegmentValide & (not math.isnan(CP2[0]))
		SegmentValide = SegmentValide & (not math.isnan(CP2[1]))
		SegmentValide = SegmentValide & (not math.isnan(CP2[2]))

		if (SegmentValide):
			TousLesSegmentsValides.InsertNextId( SegmentCourant)

# FIN DE ChercheSegmentNonParcouruEtSansNan




def ConvertitDonneesContourEnKML( MesDonneesDuContour, NomDuContour, IndiceCouleurDuContour):

	TousLesSegmentsValidesEtNonParcourus = vtk.vtkIdList()
	TousLesSommetsDansLeBonSens = vtk.vtkIdList()

	InitialiseLesSegmentsSansNanEtNonParcourus( TousLesSegmentsValidesEtNonParcourus, MesDonneesDuContour)

	compteur = 0

	while (TousLesSegmentsValidesEtNonParcourus.GetNumberOfIds() != 0):

		SegmentCourant = TousLesSegmentsValidesEtNonParcourus.GetId(0)

		compteur = compteur + 1

		SegmentInitial = MesDonneesDuContour.GetCell(SegmentCourant)
		PtIds = SegmentInitial.GetPointIds()
		PointDeBouclage = PtIds.GetId(0)
		PointCourant = PtIds.GetId(1);

		TousLesSommetsDansLeBonSens.Reset()
		PointCourant = ParcoursDansUnSens( SegmentCourant, PointCourant, PointDeBouclage, TousLesSommetsDansLeBonSens, TousLesSegmentsValidesEtNonParcourus, MesDonneesDuContour)

		if (PointCourant == PointDeBouclage):
			EcritUneLigneEnKML( TousLesSommetsDansLeBonSens, MesDonneesDuContour, NomDuContour + "(ferme)", IndiceCouleurDuContour)
		else:
			EcritUneLigneEnKML( TousLesSommetsDansLeBonSens, MesDonneesDuContour, NomDuContour + "(premiere moitie)", IndiceCouleurDuContour)

		if (PointCourant != PointDeBouclage):
			# je repars dans l autre direction

			TousLesSommetsDansLeBonSens.Reset() # VIDE LA LISTE DE LA PREMIERE MOITIE DE COURBE

			_tmp = PointCourant
			PointCourant = PointDeBouclage
			PointDeBouclage = _tmp
			PointCourant = ParcoursDansUnSens( SegmentCourant, PointCourant, PointDeBouclage, TousLesSommetsDansLeBonSens, TousLesSegmentsValidesEtNonParcourus, MesDonneesDuContour)
			EcritUneLigneEnKML( TousLesSommetsDansLeBonSens, MesDonneesDuContour, NomDuContour + "(autre moitie)", IndiceCouleurDuContour)

	# FIN DE ConvertitDonneesContourEnKML
