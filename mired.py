############################################################
# Bienvenida
from welcome import welcome_print
from file import *
from printdata import print_data
from printmessage import *
from getdata import datos, name
from exit_message import print_exit
import os

#llamamos la función bienvenida
welcome_print()

#llamamos la función para solicitar nombre
nombre = name()

#Verificamos si el archivo existe
if os.path.isfile(nombre+".user"):
    #Esto lo hacemos si ya había un usuario con ese nombre
    
    nombre, edad, estatura_m, estatura_cm, genero, pais, num_amigos = readfile(nombre)
 
else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacíamos antes
    #llamamos a la funcion datos
    print()
    genero, pais, edad, estatura_m, estatura_cm, num_amigos = datos()
        
#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print_data(nombre, genero, pais, edad, estatura_m, estatura_cm, num_amigos)
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")

#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  5. Cambiar de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
       msj = estado(nombre)

    #Código para la opción 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        friends_message(nombre, num_amigos)

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        print_data(nombre, edad, genero, pais, estatura_m, estatura_cm, num_amigos)

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = name()
        genero, pais, edad, estatura_m, estatura_cm, num_amigos = datos()
        print()
        print_data(nombre, genero, pais, edad, estatura_m, estatura_cm, num_amigos)
        print()

    #Código para cambiar de usuario 5
    elif opcion == 5:
        nombre = input("Escribe el nombre del usuario que deseas utilizar: ")
        if os.path.isfile(nombre+".user"):
            nombre, edad, estatura_m, estatura_cm, genero, pais, num_amigos = readfile(nombre)

        else:
            #En caso que el usuario no exista, notifica y continua con el mismo usuario
            print()
            print("El usuario no existe. Imposible cambiar de usuario")
            newuser = input("¿Deseas agregar un archivo con el nuevo usuario? (S/N)")
            if newuser == "S" or newuser == "s":
                nombre = name()
                genero, pais, edad, estatura_m, estatura_cm, num_amigos = datos()
            elif newuser == "N" or newuser =="n":
                print("Continuando con el usuario anterior!!")
            else:
                print("Opción no reconocida")
            
            print()

    #Código para la opción 0. Salir.
    elif opcion == 0:
        savefile(nombre, edad, estatura_m, estatura_cm, genero, pais, num_amigos)
        

    #Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print_exit()


