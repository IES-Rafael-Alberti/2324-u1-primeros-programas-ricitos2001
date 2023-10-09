def crear_masa(masa):
    return "tu índice de masa corporal es: "+str(masa)+"kg/m2"
if __name__=="__main__":
    nombre=(input("introduce tu nombre: "))
    peso=float(input("masa en kilogramos (kg): "))
    estatura=float(input("estatura en metros (m): "))
    masa=peso/(estatura**2)
    resultadomasa="tu índice de masa corporal es: ", str(masa), "kg/m2"
    resultadomasa= crear_masa (masa)
    print (resultadomasa)