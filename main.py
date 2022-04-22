
import os as os #Importer OS pour modifier des fichiers depuis Python
import csv #De meme pour l'interpreteur CSV

n = 1 # Nombre de tablettes

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


def initTab2(tabl): #Cette fonction va creer le Deuxieme Tableau
    global jours # Ramene le tableau jours cree au debut
    fich.writelines("\n<div>\n<table>\n<tr><td>"+"Heure"+"</td>") 
    for i in range(5):
        fich.writelines("<td>"+jours[i]+"</td>") # Pour chaque jour dans jours creer une case avec le jour
    fich.writelines("</tr>") # Fermer la colonne
    
    # La boucle suivante va remplir le tableau

    for i in range (10): # Pour les 10 h de la journee i:
        fich.writelines("<tr>") # creer une colonne
        fich.writelines("<td>"+str(i+8)+"h</td>") # Puis les remplir l'heure correspondante.
        for j in range (5): # Puis pour chaque jour j
            noms=[] 
            nom=""
            for k in tabl: # Pour chaque perssone k dans le dicctionaire
                a = int(k["Horaire"])-8 # A est l'heure ou la perssone k as reserve
                if i >= a and i<a+int(k["Duree"]) and jours[j] == k["Jour"]: # Si les conditions sont validés alors k as bien reserve ce creneaux, donc
                    nom=k["Nom"] # Il es rajoute au tableau des gens qui ont reserve cette case 
                    noms.append(nom)
            if len(noms) == n: # Si la taille du tableau qui contient les gens qui ont reserve cette case est plus petite que le nombre de tablettes alors tt va bien.
                c="bgcolor=\"green\"" # Case verte
            elif len(noms)>n: # Sinon
                c="bgcolor=\"red\"" # Case rouge
                nom=noms[0]
                for z in range (len(noms)-1): # Dire les gens qui ont reserve ce creneaux
                    nom+=" et "+noms[z+1]
            else: c=""

            fich.writelines("<td "+c+">"+nom+"</td>")
        fich.writelines("</tr>")
    fich.writelines("</table></div>") # Fermer le tableau et le div.
 

# Generer les 2 tableaux
initTab(table)
initTab2(table)

fich.writelines("\n</div>") # Un div perdu qui casse surement tout si je l'enleve


# Finir la page
fich.writelines(["</ul>\n","</body>\n","</html>\n"])
fich.close() # Ne pas oublier de fermer le .csv sinon,,,

print("Programme fini....tu peux respirer")