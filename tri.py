ofi1 = open('fichier1.txt', 'r')
ofi2 = open('fichier2.txt', 'w')
text2= []
text1 = ofi1.read()
ofi1.close()
cpt = 0
fonction = ""
for y in range(len(text1)):
	if text1[y] == '/' and text1[y+1] == '/':
		word = "" + text1[y:y+9]
	else:
		word = ""

	if word == "// change" or (y+1)==len(text1):
		print("fonction: " + fonction)
		text2.append(fonction)
		fonction =""
	fonction = fonction + text1[y]

text2.sort()

for fonction in text2:
	ofi2.write(fonction)
ofi2.close()