def name():
    #Solicita nombre
    nombre = input("Para empezar, dime como te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()
    return nombre
    
def datos():
    # Solicitud de género
    genero = input("Escribe tu género: ")
    print()

    # Solicita el país de nacimiento
    pais = input("Escribe tu pais de nacimiento: ")
    print()

    # Calculo de edad
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    edad = 2021-agno
    print()

    # Calculo de estatura
    estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Damelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    print()

    # Cantidad de amigos
    num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
    return(genero, pais, edad, estatura_m, estatura_cm, num_amigos)
