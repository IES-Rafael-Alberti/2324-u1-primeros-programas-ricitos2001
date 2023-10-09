def crear_resultado(suma):
    return "el resultado es: "+ str(suma)
if __name__=="__main__":
    suma=(int(input("primer numero: ")) + int(input("segundo numero: ")) + int(input("tercer numero: ")))
    resultado="el resultado es: ", str(suma)
    resultado= crear_resultado (suma)
    print (resultado)