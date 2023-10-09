def crear_mayuscula(fraseconvocalmayuscula):
    return fraseconvocalmayuscula

if __name__ == "__main__":
    frase=input("escribe una frase: ")
    vocal=input("escribe una vocal: ")
    vocalminuscula=vocal.lower()
    vocalmayuscula=vocal.upper()
    fraseconvocalmayuscula = frase.replace(vocalminuscula, vocalmayuscula)
    if len(vocal) == 1 and vocal.isalpha():
        resultado=fraseconvocalmayuscula
        resultado=crear_mayuscula(fraseconvocalmayuscula)
        print(resultado)
    else:
        print("error sintactico. por favor, introduce una sola letra como vocal.")