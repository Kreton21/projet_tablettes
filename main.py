import os as os
import csv
d=open("Test.csv")
table=list(csv.DictReader(d,delimiter=","))
jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
print("Tout marche bien pr le moment")
fich = open("index.html", "w")
fich.writelines(
["<!DOCTYPE html>\n","<html>\n", "<head>\n","<title >Table de multiplication </title>\n",\
"</head>\n",
 "<body>\n","<h1> Reserver Tablettes !</h1>","<ul>\n"])

fich.writelines("<div>")
fich.writelines("<table>")
def initTab(tabl):
    fich.writelines("<tr>"+"<td>"+"Nom"+"</td>"+"<td>"+"Jour"+"</td>"+"<td>"+"Horaire"+"</td>"+"<td>"+"Durée"+"</td>"+"</tr>")
    for i in tabl:
        fich.writelines("<tr>")
        genereTab(table,i)
        fich.writelines("</tr>")
def genereTab(tabl,i):
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
                if i == a and jours[j] == k["Jour"]:
                    nom=k["Nom"]
                    noms.append(nom)
            if len(noms) == 1:
                c="bgcolor=\"green\""
            elif len(noms)>1:
                c="bgcolor=\"red\""
                nom=noms[0]
                for i in range (len(noms)-1):
                    nom+=" et "+noms[i+1]
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