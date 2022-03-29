import os as os
import csv
d=open("/test.csv")
table=list(csv.DictReader(d,delimiter=","))



f = open("index.txt", "w")
f.writelines("test")
f.close()


fich = open("index.html", "w")
fich.writelines(
["<!DOCTYPE html>\n","<html>\n", "<head>\n","<title>\
Table de multiplication </title>\n", "</head>\n",
 "<body>\n","<h1> C'est le titre !</h1>","<ul>\n"])

fich.writelines(genere_tableHTML(5))

fich.writelines(["</ul>\n","</body>\n","</html>\n"])
fich.close()
