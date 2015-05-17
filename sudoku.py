import array
import turtle

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


def carre(sudoku):
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
	sudoku = [[0]*10]*10
	for x in range(0,9):
		for y in range(0,9):			
				c = x%3
				l = (y//3)
				sudoku[c][l] = carres[x][y]
	return sudoku


def ligne(sudoku):
	lignes = []
	for x in range(0,9):
		lignes.append(sudoku[x])
	return lignes

def colonne(sudoku):
	colonnes = []
	for y in range(0,9):
		colonne = []
		for x in range(0,9):
			colonne.append(sudoku[x][y])
		colonnes.append(colonne)
	return colonnes

def isManquant(tableau,nb):
	for x in range(0,9):
		if tableau[x] == nb:
			return False
	return True
def isPresent(tableau,nb):
	for x in range(0,9):
		if tableau[x] == nb:
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
	print(match)
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

def match(nbs,colonnes,lignes,c,l):
		match = {}
		trouve = False	
		for nb in nbs:
			colonnePresent = isPresent(colonnes[c],nb) 
			lignePresent = isPresent(lignes[l],nb)
			trouve = not colonnePresent and not lignePresent
			match[nb] = trouve
		return match

def affichage(sudoku):
	
	for y in range(0,10):
		turtle.up()
		turtle.goto(0,y*20)
		turtle.down()
		turtle.goto(180,y*20)
		turtle.up()


	for x in range(0,10):
		turtle.up()
		turtle.goto(x*20,0)
		turtle.down()
		turtle.goto(x*20,180)
		turtle.up()

	for y in range(0,9):
		for x in range(0,9):
			turtle.up()
			turtle.goto(x*20+10,y*20+3)
			turtle.write(sudoku[x][y], True, align="center")
	turtle.exitonclick()

carres = carre(sudoku)
lignes = ligne(sudoku)
colonnes = colonne(sudoku)

sudoku = carresToSudoku(carres)
"""for i in range(0,10):	
	cpt = 0
	for carre in carres:
		nbs= nbManquant(carre)
		print(nbs)
		for x in range(0,9):
			case = carre[x]
			if case == 0 :				
				c = x%3+(cpt%3)*3
				l = (x//3)+(cpt//3)
				print("lignes: " + str(l) + " colonne: " + str(c))	
				matchs = match(nbs,colonnes,lignes,c,l)
				carre[x]=doublon(matchs)

		cpt += 1

	print(i)
	print(carres)

affichage(sudoku)"""
print(carres)
print(sudoku)
