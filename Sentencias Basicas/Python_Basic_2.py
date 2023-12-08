import random
#declaracion de varibles
colores = ['amarillo', 'azul', 'verde', 'rojo']
colores_usados = []
usuarios = [{'Nombre':'Josep'}, {'Nombre':'Claudio'}, {'Nombre':'Isabel'}, {'Nombre':'Sheila'}]
#rutina añadir color a la lista
def añadirColor():
    global colores
    color = input("Introduce el nombre del color\n")
    if color not in colores:
        colores.append(color.lower())
    else:
        print("El color existe prube otra vez\n")
        añadirColor()
    return True
#rutina lista de colores
def mostrarColores():
    global colores
    print("Lista de colores:\n")
    for i in colores:
        print("{}\n".format(i))
    return True
#rutina ordenar lista de colores
def odenarColores():
    global colores
    colores.sort()
    return True
def listausuarios(users):
    l_users = []
    for i in users:
        l_users.append(i.get("Nombre"))
    return l_users
#rutina añadir usuario a la lista
def añadirUsuarios():
    global usuarios,colores
    user = input("Introducir nombre de l'usuario:\n")
    if user not in listausuarios(usuarios):
        usuarios.append({"Nombre":user})
        if len(usuarios)>len(colores):
            añadirColor()
    else:
        print("El usuario ja existe:\n")
    return True
#rutina para assinar el usuario el color
def assignarColor():
    global usuarios,colores
    assignado = False
    for i in usuarios:
        key = i.keys()
        if "Color" not in key:
            while assignado == False:
                indice = random.randint(0,len(colores)-1)
                if colores[indice] not in colores_usados:
                    i["Color"] = colores[indice]
                    print(i.items())
                    colores_usados.append(colores[indice])
                    assignado = True
        assignado = False
    return True
def mostrarUsuarios(users):
    nombres = sorted(listausuarios(users))
    j =0
    for i in nombres:
        print("Nombre: ",i,"--> Color:", users[j].get("Color"),"--> Indice",j)
        j+=1

#rutina para eliminar usuarios
def eliminarUsuarios():
    global usuarios, colores_usados
    copy_users = usuarios.copy()
    mostrarUsuarios(copy_users)
    try:
        indice = int(input("Entra el indice del usaurio a borrar:\n"))
    except Exception as keyboard:
        eliminarUsuarios()
    color = usuarios[indice].get("Color")
    del usuarios[indice]
    colores_usados.remove(color)
    return True
#rutina para eliminar usuarios
def mostrarNombreusuarios():
    global usuarios
    print(listausuarios(usuarios))
    return True
#rutina par salir del meun
def salir():
    print("Gracias por su tiempo\n")
    return False
def switch(opcion):
    diccionario = {
    "1": "añadirColor()",
    "2": "mostrarColores()",
    "3": "odenarColores()",
    "4": "añadirUsuarios()",
    "5": "assignarColor()",
    "6": "eliminarUsuarios()",
    "7": "mostrarNombreusuarios()",
    "8": "salir()"
    }
    return eval(diccionario.get(opcion))
def menu():
     print("""Selecciona una opción:
    1) Añadir colores a la lista
    2) Mostrar listado de colores
    3) Ordenar listado de colores alfabéticamente
    4) Añadir usuarios
    5) Asignar colores a cada usuario
    6) Eliminar usuarios
    7) Mostrar usuarios, solo el Nombre
    8) Salir""")
while(True):
    menu()
    opcion = input()
    try:
        continuar = switch(opcion)
        if continuar == False:
            break
    except Exception as r:
        print("Selecciona una opcio válida")
   