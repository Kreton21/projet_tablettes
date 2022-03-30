import os as os
import csv
d=open("Test.csv")
table=list(csv.DictReader(d,delimiter=","))
jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
print(table)
fich = open("index.html", "w")
fich.writelines(
["<!DOCTYPE html>\n","<html>\n", "<head>\n","<title >Table de multiplication </title>\n",\
"\n<script src=\"https://unpkg.com/@popperjs/core@2\"></script>",\
"\n<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\">",\
"\n<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p\" crossorigin=\"anonymous\"></script>",\
"\n<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js\"></script>",\
"\n</head>\n",\
 "<body >\n","<div style=\"height: 100%;\
 background: repeating-linear-gradient(\
  125deg,\
  #3d3d3d,\
  #3d3d3d 30px,\
  #303030 50px,\
  #303030 50px\
)\";\>"])

fich.writelines("\n<div class=\"container\" style=\"padding-top: 20px;padding-bottom: 500px\">")
fich.writelines("\n<table class=\"table table-bordered table-dark table-striped table-hover >\"")
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
    fich.writelines("<div class=\"container\">")
    fich.writelines("<table class=\"table table-bordered table-dark table-striped table-hover>\">")
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
                c="class=\"table-success\""
            elif len(noms)>1:
                c="class=\"table-danger\""
                nom=noms[0]
                for i in range (len(noms)-1):
                    nom+=" et "+noms[i+1]
            else: c=""

            fich.writelines("<td "+c+">"+nom+"</td>")
        fich.writelines("</tr>")

initTab(table)
initTab2(table)
fich.writelines("</div>")
fich.writelines("\n<a tabindex=\"0\" class=\"btn btn-lg btn-danger\" role=\"button\" data-bs-toggle=\"popover\" data-bs-trigger=\"hover focus\" title=\"Dismissible popover\" data-bs-content=\"And here's some amazing content. It's very engaging. Right?\">Testo</a>")
fich.writelines("\n<script>var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle=\"popover\"]'));var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {return new bootstrap.Popover(popoverTriggerEl)})</script>")
fich.writelines("\n<script>var popover = new bootstrap.Popover(document.querySelector('.popover-dismiss'), {  trigger: 'focus'})</script>")
fich.writelines("\n</div>")
fich.writelines(["</body>\n","</html>\n"])
fich.close()
