import os as os #Importer OS pour modifier des fichiers depuis Python
import csv #De meme pour l'interpreteur CSV


d=open("Test.csv") # Ouvrir le fichier "Test.csv" sous la variable d
table=list(csv.DictReader(d,delimiter=",")) # Transformer ce fichier en tableau de dictionaires utilisables dans le programme

print("Tout marche bien pr le moment")

fich = open("index.html", "w")
fich.writelines( # Initialisation du fichier HTML avec tt son boilerplate
["<!DOCTYPE html>\n","<html>\n", "<head>\n","<title >Table de multiplication </title>\n",\
"</head>\n",
 "<body>\n","<h1> Reserver Tablettes !</h1>","\n<ul>\n","<div>\n<table>"])


jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]


def initTab(tabl): #Cette fonction crée les colonnes du premier tableau
    fich.writelines("<tr>"+"<td>"+"Nom"+"</td>"+"<td>"+"Jour"+"</td>"+"<td>"+"Horaire"+"</td>"+"<td>"+"Durée"+"</td>"+"</tr>")
    for i in tabl:   #Pour nombre de perssones dans le fichier CSV faire:
        fich.writelines("\n<tr>")  #Creeer une colonne de tableau 
        genereTab(table,i)  # Et ensuite la remplir avec la fonction suivante
        fich.writelines("\n</tr>")

    
def genereTab(tabl,i): # Pour chaque case du tableau introduire l'info correspondante.
    fich.writelines("<td>"+str(i["Nom"])+"</td>")
    fich.writelines("<td>"+str(i["Jour"])+"</td>")
    fich.writelines("<td>"+str(i["Horaire"])+"h</td>")
    fich.writelines("<td>"+str(i["Duree"])+"h</td>")
def initTab2(tabl):
    global jours
    fich.writelines("<div>")
    fich.writelines("<table>")
    fich.writelines("<tr>")
    fich.writelines("<td>"+"Heure"+"</td>")
    for i in range(5):
        fich.writelines("<td>"+jours[i]+"</td>")
    fich.writelines("</tr>")
    
    for i in range (10):
        fich.writelines("<tr>")
        fich.writelines("<td>"+str(i+8)+"h</td>")
        for j in range (5):
            noms=[]
            nom=""
            for k in tabl:
                a = int(k["Horaire"])-8
                if i >= a and i<a+int(k["Duree"]) and jours[j] == k["Jour"]:
                    nom=k["Nom"]
                    noms.append(nom)
            if len(noms) == 1:
                c="bgcolor=\"green\""
            elif len(noms)>1:
                c="bgcolor=\"red\""
                nom=noms[0]
                for z in range (len(noms)-1):
                    nom+=" et "+noms[z+1]
            else: c=""

            fich.writelines("<td "+c+">"+nom+"</td>")
        fich.writelines("</tr>")
    fich.writelines("</table>")
    fich.writelines("</div>")



initTab(table)
initTab2(table)
fich.writelines("</div>")



fich.writelines(["</ul>\n","</body>\n","</html>\n"])
fich.close()
print("Programme fini....tu peux respirer")