def friends_message(nombre, num_amigos):
    mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
    print()
    for i in range(num_amigos):
        nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
        print("--------------------------------------------------")
        print(nombre, "dice:", "@"+nombre_amigo, mensaje)
        print("--------------------------------------------------")


def estado(nombre):
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")
    return mensaje
