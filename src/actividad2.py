def crear_importe (importe):
    return "importe total: "+str(importe)+"€"
if __name__=="__main__":
    nombre=(input("introduce tu nombre: "))
    horas=int(input("horas de trabajo: "))
    coste=int(input("Coste por hora: "))
    importe=horas*coste
    importetotal = "importe total: ", str(importe),"€"
    importetotal = crear_importe (importe)
    print (importetotal)

