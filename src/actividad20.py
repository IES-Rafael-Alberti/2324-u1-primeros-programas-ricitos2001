def crear_numerosindigitos(formatoendigitos):
    return "su numero sin digitos es: "+str(formatoendigitos)

if __name__=="__main__":
    numero = input("escriba un numero de telefono: ")
    partes = numero.split("-") 
    if len(partes) >= 2 and partes[0] == "+34":
        formatoendigitos = int(partes[1])
        formatocorrecto= "su numero sin digitos es: ", str(formatoendigitos)
        formatocorrecto=crear_numerosindigitos(formatoendigitos)
        print(formatocorrecto)
