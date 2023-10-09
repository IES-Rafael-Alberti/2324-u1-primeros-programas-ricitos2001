def crear_cociente(cociente):
    return "el cociente es: "+str(cociente)
def crear_resto(resto):
    return "el resto es: "+str(resto)
if __name__=="__main__":
    numero1=int(input("primer numero: "))
    numero2=int(input("segundo numero: "))
    cociente=numero1/numero2
    resto=numero1%numero2
    resultadocociente= "el resto es: ", str(resto)
    resultaadoresto= "el resto es: ", str(resto)
    resultadocociente= crear_cociente(cociente)
    resultaadoresto= crear_resto(resto)
    print (resultadocociente)
    print (resultaadoresto)