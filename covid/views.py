from covid import app
import csv
import json

@app.route("/provincias")
def provincias():
    fichero = open("data/provincias.csv", "r", encoding="utf8")
    csvreader = csv.reader(fichero, delimiter=",")

    lista = []
    for registro in csvreader:
        d = {'codigo': registro[0], 'valor': registro[1]}
        lista.append(d)

    fichero.close()
    print(lista)
    return json.dumps(lista)




@app.route("/provincia/<codigoProvincia>")
def laprovincia(codigoProvincia):
    fichero = open("data/provincias.csv", "r", encoding="utf8")
    
    dictreader = csv.DictReader(fichero,fieldnames=['codigo', 'provincia'])
    for registro in dictreader:
        if registro['codigo'] == codigoProvincia:
            fichero.close()
            return registro['provincia']

    fichero.close()
    return "La provincia no existe. Largo de aqui!!!"