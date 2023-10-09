def crear_resultado(suma):
    return "el resultado es: "+suma
if __name__=="__main__":
    numero1=int(input("primer numero: "))
    numero2=int(input("segundo numero: "))
    numero3=int(input("tercer numero: "))
    suma=numero1+numero2+numero3
    resultado="el resultado es: ", suma
    resultado= crear_resultado (suma)
    print (resultado)