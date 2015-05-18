import array
import turtle
import numpy

def sudokuToCarres(sudoku):
	carres = []
	for x1 in range(0,3):
		for y1 in range(0,3):
			carre = []
			for x in range((3*x1),3*(x1+1)):
				for y in range((3*y1),3*(y1+1)):
					carre.append(sudoku[x][y])
			carres.append(carre)
	return carres

def carresToSudoku(carres):
	sudoku = []
	for x in range(0,9):
		ligne = []
		for y in range(0,3):
			for z in range(0,3):
				ligne.append(carres[y+(x//3)*3][z+(x%3)*3])
		sudoku.append(ligne)
	return sudoku


def sudokuToLignes(sudoku):
	lignes = []
	for x in range(0,9):
		lignes.append(sudoku[x])
	return lignes

def lignesToSudoku(lignes):
	sudoku = []
	for ligne in lignes:
		sudoku.append(ligne)
	return sudoku

def sudokuToColonnes(sudoku):
	colonnes = []
	for y in range(0,9):
		colonne = []
		for x in range(0,9):
			colonne.append(sudoku[x][y])
		colonnes.append(colonne)
	return colonnes

def colonnesToSudoku(colonnes):
	sudoku = []
	for x in range(0,9):
		ligne = []
		for colonne in colonnes:
			ligne.append(colonne[x])
		sudoku.append(ligne)
	return sudoku

def isManquant(tableau,nb):
	for case in tableau:
		if case == nb:
			return False
	return True
def isPresent(tableau,nb):
	for case in tableau:
		if case == nb:
			return True
	return False

def nbManquant(tableau):
	nbs = []
	for x in range(1,10):
		if (isManquant(tableau,x)):
			nbs.append(x)
	return nbs

def doublon(match):
	first = False
	doublon = False
	nbMatch = 0
	for nb, value in match.items():
		if first and value:
			doublon = True
		first = value or first
		if(not doublon and value):
			nbMatch = nb
	if not doublon:
		return nbMatch
	else:
		return 0

def match(nbs,tableau1,tableau2):
		match = [False]*10
		trouve = False	
		for nb in nbs:
			tableau1Present = isPresent(tableau1,nb) 
			tableau2Present = isPresent(tableau2,nb)
			trouve = not tableau1Present and not tableau2Present
			match[nb] = trouve
		return match

def affichage(sudoku):
	turtle.speed(0)
	turtle.delay(1)
	cpt = 0
	for y in range(-5,5):
		if cpt%3 == 0 :
			turtle.pensize(2)
		else:
			turtle.pensize(1)
		cpt += 1
		turtle.up()
		turtle.goto(-180,(y*40)+20)
		turtle.down()
		turtle.goto(180,(y*40)+20)
		turtle.up()

	cpt = 0
	for x in range(-5,5):
		if cpt%3 == 0 :
			turtle.pensize(2)
		else:
			turtle.pensize(1)
		cpt += 1
		turtle.up()
		turtle.goto((x*40)+20,-180)
		turtle.down()
		turtle.goto((x*40)+20,180)
		turtle.up()

	x = -4
	for l in range(0,9):
		y = 4
		for c in range(0,9):
			turtle.up()
			turtle.goto(x*40,(y*40)-10)
			if sudoku[l][c] != 0:
				turtle.write(sudoku[l][c], True, align="center",  font=("Arial", 16, "normal"))
			y -= 1
		x += 1

def iteration(sudoku):
	lignes = sudokuToLignes(sudoku)
	colonnes = sudokuToColonnes(sudoku)	
	carres = sudokuToCarres(sudoku)
	cpt = 0
	for ligne in lignes:
		nbs= nbManquant(ligne)
		ligneProvisoire = [[0]]*9
		for x in range(0,9):		
			ligneProvisoire[x]=[ligne[x]]
			case = ligne[x]
			if case == 0 :
				matchs = match(nbs,colonnes[x],carres[(x//3) + (cpt//3)*3])
				ligneProvisoire[x].append(doublon(matchs))
		for x in range(0,9):
			if len(ligneProvisoire[x]) == 2:
				ligne[x]=ligneProvisoire[x][1] 
		cpt +=1
	sudoku = lignesToSudoku(lignes)
	
	colonnes = sudokuToColonnes(sudoku)
	cpt = 0
	for colonne in colonnes:
		nbs= nbManquant(colonne)
		colonneProvisoire = [[0]]*9
		for x in range(0,9):		
			colonneProvisoire[x]=[colonne[x]]
			case = colonne[x]
			if case == 0 :
				matchs = match(nbs,lignes[x],carres[(x%3) + (cpt%3)])
				colonneProvisoire[x].append(doublon(matchs))
		for x in range(0,9):
			if len(colonneProvisoire[x]) == 2:
				colonne[x]=colonneProvisoire[x][1] 
		cpt +=1
	sudoku = colonnesToSudoku(colonnes)
	
	carres = sudokuToCarres(sudoku)
	
	sudokuProvisoire2 = carresToSudoku(carres)


	return sudoku

def possibleCarres(carres, colonnes, lignes):
	cpt = 0
	matchCarres=[]
	for carre in carres:
		matchCarre = []
		nbs= nbManquant(carre)
		for x in range(0,9):		
			case = carre[x]
			matchs = [False]*10
			if case == 0 :
				matchs = match(nbs,colonnes[(x%3) + (cpt%3)*3],lignes[(x//3) + (cpt//3)])
			matchCarre.append(matchs)
		matchCarres.append(matchCarre)
		cpt +=1
	return matchCarres


"""
sudoku = [
[4,0,5,0,0,3,2,0,9],
[0,0,0,0,0,0,0,4,0],
[1,7,0,0,0,5,0,0,0],
[6,0,0,5,0,0,4,0,2],
[3,0,0,9,0,7,0,0,1],
[2,0,7,0,0,4,0,0,3],
[0,0,0,7,0,0,0,5,4],
[0,6,0,0,0,0,0,0,0],
[7,0,1,3,0,0,9,0,6]]
"""
sudoku = [
[6,0,9,0,0,5,2,0,0],
[0,5,1,4,0,8,0,0,7],
[7,4,0,0,6,0,8,9,0],
[0,1,0,6,0,0,0,7,8],
[3,9,0,0,0,0,0,1,6],
[5,6,0,0,0,4,0,2,0],
[0,3,4,0,2,0,0,5,9],
[8,0,0,9,0,3,1,6,0],
[0,0,6,5,0,0,3,0,4]]
"""
affichage(sudoku)
toto = "y"
while toto == "y" :
	sudoku = iteration(sudoku)
	for i in range(0,9):
		print(sudoku[i])
	carres = sudokuToCarres(sudoku)
	print("")
	for i in range(0,9):
		print(carres[i])
	sudoku = carresToSudoku(carres)
	print("")
	for i in range(0,9):
		print(sudoku[i])
	print("")
	affichage(sudoku)
	toto = input("continuer?")
"""

lignes = sudokuToLignes(sudoku)
colonnes = sudokuToColonnes(sudoku)	
carres = sudokuToCarres(sudoku)
matchSudoku = [[[False]*10]*9]*9
matchSudoku2 = carresToSudoku(possibleCarres(carres,colonnes,lignes))
for y in range(0,9):
    for x in range(0,9):
        for z in range(0,10):
            valeur1 = matchSudoku[y][x][z]
            valeur2 = matchSudoku2[y][x][z]
            test =  valeur1 or valeur2
            matchSudoku[y][x][z] = test

print("toto")
