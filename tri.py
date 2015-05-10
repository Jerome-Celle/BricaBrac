fichierInput = input('Le nom du fichier à trier?\n')
delimiteur = input('Le delimiteur de fin de fonction?\n')
ofiInput = open(fichierInput, 'r')
ofiOutput = open('fichierOutput.txt', 'w')
tableauFonction= []
text = ofiInput.read()
ofiInput.close()
fonction = ""
for y in range(len(text)):
	fonction = fonction + text[y]
	if text[y:y+9] == "// change" or (y+1)==len(text):
		tableauFonction.append(fonction)
		fonction =""

tableauFonction.sort()

for fonction in tableauFonction:
	ofiOutput.write(fonction)
ofiOutput.close()