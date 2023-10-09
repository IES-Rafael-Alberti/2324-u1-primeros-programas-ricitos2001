def crear_primeraño (primeraño):
    return "primer año: "+str(primeraño)+"€"
def crear_segundoaño (segundoaño):
    return "segundo año: "+str(segundoaño)+"€"
def crear_terceraño (terceraño):
    return "tercer año: "+str(terceraño)+"€"
if __name__=="__main__":
    nombre=(input("nombre de usuario: "))
    cantidad=int(input("cantidad de dinero: "))
    interes=float(0.04)
    primeraño=cantidad+(cantidad*interes)
    segundoaño=primeraño+(primeraño*interes)
    terceraño=segundoaño+(segundoaño*interes)
    dineroprimeraño = "primer año: ", str(primeraño),"€"
    dinerosegundoaño = "segundo año: ", str(segundoaño),"€"
    dineroterceraño = "tercer año: ", str(terceraño),"€"
    dineroprimeraño = crear_primeraño (primeraño)
    dinerosegundoaño = crear_segundoaño (segundoaño)
    dineroterceraño = crear_terceraño (terceraño)
    print (dineroprimeraño)
    print (dinerosegundoaño)
    print (dineroterceraño)