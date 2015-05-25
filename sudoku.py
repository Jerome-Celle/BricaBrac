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

	y = 4
	for l in range(0,9):
		x = -4
		for c in range(0,9):
			turtle.up()
			turtle.goto(x*40,(y*40)-10)
			if sudoku[l][c] != 0:
				turtle.write(sudoku[l][c], True, align="center",  font=("Arial", 16, "normal"))
			x += 1
		y -= 1


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

def possibleColonnes(carres, colonnes, lignes):
    cpt = 0
    matchColonnes=[]
    for colonne in colonnes:
        matchColonne = []
        nbs= nbManquant(colonne)
        for x in range(0,9):
            case = colonne[x]
            matchs = [False]*10
            if case == 0 :
                matchs = match(nbs,lignes[x],carres[(x%3) + (cpt%3)])
            matchColonne.append(matchs)
        matchColonnes.append(matchColonne)
        cpt +=1
    return matchColonnes

def possibleLignes(carres, colonnes, lignes):
    cpt = 0
    matchLignes=[]
    for ligne in lignes:
        matchLigne = []
        nbs= nbManquant(ligne)
        for x in range(0,9):
            case = ligne[x]
            matchs = [False]*10
            if case == 0 :
                matchs = match(nbs,colonnes[x],carres[(x//3) + (cpt//3)*3])
            matchLigne.append(matchs)
        matchLignes.append(matchLigne)
        cpt +=1
    return matchLignes




sudoku = [
[7,0,6,0,0,4,9,0,8],
[0,0,0,0,0,0,0,7,0],
[1,2,0,0,0,8,0,0,0],
[4,0,0,1,0,0,8,0,3],
[9,0,0,8,0,6,0,0,4],
[3,0,1,0,0,2,0,0,7],
[0,0,0,2,0,0,0,8,9],
[0,1,0,0,0,0,0,0,0],
[6,0,3,4,0,0,2,0,1]]
"""
sudoku = [
[0,4,9,1,0,2,8,3,5],
[0,8,0,7,0,0,0,0,0],
[0,0,1,0,0,9,7,4,0],
[0,2,6,0,3,4,0,7,0],
[4,1,0,0,0,0,0,5,3],
[0,3,0,9,1,0,6,2,0],
[0,9,8,2,0,0,4,0,0],
[0,0,0,0,0,3,0,8,0],
[5,7,4,6,0,8,3,1,0]]"""

for i in range(0,20):
    lignes = sudokuToLignes(sudoku)
    colonnes = sudokuToColonnes(sudoku)	
    carres = sudokuToCarres(sudoku)
    matchSudoku = [[[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10],
                   [[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10,[False]*10]]

    """
    matchSudoku2 = carresToSudoku(possibleCarres(carres,colonnes,lignes))
    for y in range(0,9):
        for x in range(0,9):
            for z in range(0,10):
                valeur1 = matchSudoku[y][x][z]
                valeur2 = matchSudoku2[y][x][z]
                test =  valeur1 or valeur2
                matchSudoku[y][x][z] = test

    carres = sudokuToCarres(sudoku)
    matchcarres = sudokuToCarres(matchSudoku)
    for z in range(0,9):
        for nb in range(1,10):
            doublon = False
            position = -1
            for x in range(0,9):
                if matchcarres[z][x][nb]:
                    if doublon == False:
                        position = x
                        doublon = True
                    elif doublon == True:
                        position = -1 
            if position != -1:
                carres[z][position]=nb
    sudoku = carresToSudoku(carres)
    """
    
    lignes = sudokuToLignes(sudoku)
    colonnes = sudokuToColonnes(sudoku)	
    carres = sudokuToCarres(sudoku)
    matchSudoku2 = lignesToSudoku(possibleLignes(carres,colonnes,lignes))
    for y in range(0,9):
        for x in range(0,9):
            for z in range(0,10):
                valeur1 = matchSudoku[y][x][z]
                valeur2 = matchSudoku2[y][x][z]
                test =  valeur1 or valeur2
                matchSudoku[y][x][z] = test

    matchlignes = sudokuToLignes(matchSudoku)
    for z in range(0,9):
        for nb in range(1,10):
            doublon = False
            position = -1
            for x in range(0,9):
                if matchlignes[z][x][nb]:
                    if doublon == False:
                        position = x
                        doublon = True
                    elif doublon == True:
                        position = -1 
            if position != -1:
                lignes[z][position]=nb
    sudoku = lignesToSudoku(lignes)

    lignes = sudokuToLignes(sudoku)
    colonnes = sudokuToColonnes(sudoku)	
    carres = sudokuToCarres(sudoku)
    matchSudoku2 = colonnesToSudoku(possibleColonnes(carres,colonnes,lignes))
    for y in range(0,9):
        for x in range(0,9):
            for z in range(0,10):
                valeur1 = matchSudoku[y][x][z]
                valeur2 = matchSudoku2[y][x][z]
                test =  valeur1 or valeur2
                matchSudoku[y][x][z] = test

    matchcolonnes = sudokuToColonnes(matchSudoku)
    for z in range(0,9):
        for nb in range(1,10):
            doublon = False
            position = -1
            for x in range(0,9):
                if matchcolonnes[z][x][nb]:
                    if doublon == False:
                        position = x
                        doublon = True
                    elif doublon == True:
                        position = -1 
            if position != -1:
                colonnes[z][position]=nb
    sudoku = colonnesToSudoku(colonnes)


affichage(sudoku)
print("toto")
