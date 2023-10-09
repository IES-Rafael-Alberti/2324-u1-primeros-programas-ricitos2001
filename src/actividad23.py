def modificarEmail(email):
    if any(c.isalpha() for c in email) and "@" in email:
        nombre, dominio = email.split("@")
        emailMod = nombre + "@ceu.es"
        return emailMod
    else:
        return "Correo electrónico inválido. Debe contener al menos una letra y una arroba (@)."

if __name__ == "__main__":
    email = input("Escriba su correo electronico: ")
    texto = modificarEmail(email)
    print("Tu correo es ", texto)