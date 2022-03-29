import os as os
import csv
d=open("Test.csv")
table=list(csv.DictReader(d,delimiter=","))
jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
print(table)
fich = open("index.html", "w")
fich.writelines(
["<!DOCTYPE html>\n","<html>\n", "<head>\n","<title >Table de multiplication </title>\n",\
"<script src=\"https://unpkg.com/@popperjs/core@2\"></script>",\
"<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\">",\
"<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p\" crossorigin=\"anonymous\"></script>",\
"<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js\"></script>",\
"</head>\n",\
 "<body>\n","<h1> Reserver Tablettes !</h1>","<ul>\n"])

fich.writelines("<div>")
fich.writelines("<table class=\"table table-bordered >\"")
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

initTab(table)
initTab2(table)
fich.writelines("</div>")



fich.writelines(["</ul>\n","</body>\n","</html>\n"])
fich.close()
