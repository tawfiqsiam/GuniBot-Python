from fcts.lang import fr,en
import csv

def save_fr():
    text = str()
    with open('translation/french2.csv','w',encoding='utf-8',newline='') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for objet in fr.__dict__:
            if objet.startswith("_"):
                continue
            for k,v in  eval("fr."+objet).items():
                try:
                    f.writerow([k,v,eval("en."+objet)[k]])
                except KeyError:
                    f.writerow([k,v,""])
            f.writerow([])

def save_en():
    text = str()
    for objet in en.__dict__:
        if objet.startswith("_"):
            continue
        for v in  eval("en."+objet).values():
            text = text+str(v).replace("\n","  ")+"\n"
        text += "\n"
    with open('translation/english.text','w',encoding='utf-8') as fichier:
        fichier.write(text)
