def readfile(nombre):
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().strip()
    #nombre = nombre.strip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    genero = archivo_usuario.readline().strip()
    #genero = genero.strip()
    pais = archivo_usuario.readline().strip()
    #pais = pais.strip()
    num_amigos = int(archivo_usuario.readline())
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, edad, estatura_m, estatura_cm, genero, pais, num_amigos)


def savefile(nombre, edad, estatura_m, estatura_cm, genero, pais, num_amigos):
    print("Has decidido salir. Guardando perfil en ", nombre, ".user")
    archivo_usuario = open(nombre+".user", "w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(((estatura_m + 99)+ estatura_cm)/100)+"\n")
    archivo_usuario.write(genero+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(str(num_amigos))
    #Una vez que se registran los datos se cierra el archivo
    archivo_usuario.close()
    print("Archivo ", nombre+".user"," guardado")
