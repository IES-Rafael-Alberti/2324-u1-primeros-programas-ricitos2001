def crear_repeticiones(repeticiones):
    return repeticiones
if __name__ == "__main__":
    nombre = input("escriba su nombre: ")
    numero = int(input("numero de repeticiones: "))
    repeticiones = ""
    if numero > 0:
        for contador in range(numero):
            repeticiones += nombre + "\n"
    texto = repeticiones
    texto = crear_repeticiones(repeticiones)
    print(texto)