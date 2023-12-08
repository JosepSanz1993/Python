#declaracion de variables
puntos_iniciales = [121,121,121,121] #puntos de cada jugador
puntos_jug1 =[] #puntos jugador 1
puntos_jug2 =[] #puntos jugador 2
puntos_jug3 =[] #puntos jugador 3
puntos_jug4 =[] #puntos jugador 4
jug1 = input("Introduce el nombre del jugador 1:\n")
jug2 = input("Introduce el nombre del jugador 2:\n")
jug3 = input("Introduce el nombre del jugador 3:\n")
jug4 = input("Introduce el nombre del jugador 4:\n")
#Ronda 1

print("Ronda 1:\n")
puntos_jug1.append(puntos_iniciales[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug1))))
puntos_jug1[0] = puntos_jug1[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug1)))
puntos_jug1[0] = puntos_jug1[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug1)))
puntos_jug2.append(puntos_iniciales[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug2))))
puntos_jug2[0] = puntos_jug2[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug2)))
puntos_jug2[0] = puntos_jug2[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug2)))
puntos_jug3.append(puntos_iniciales[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug3))))
puntos_jug3[0] = puntos_jug3[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug3)))
puntos_jug3[0] = puntos_jug3[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug3)))
puntos_jug4.append(puntos_iniciales[3] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug4))))
puntos_jug4[0] = puntos_jug4[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug4)))
puntos_jug4[0] = puntos_jug4[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug4)))

if puntos_jug1[0]<=0 or puntos_jug2[0]<=0 or puntos_jug3[0]<=0 or puntos_jug4[0]<=0:
    if puntos_jug1[0]<=0:
        print("El {} con {} ha ganado\n".format(jug1,puntos_jug1[0]))
    if puntos_jug2[0]<=0:
        print("El {} con {} ha ganado\n".format(jug2,puntos_jug2[0]))
    if puntos_jug3[0]<=0:
        print("El {} con {} ha ganado\n".format(jug3,puntos_jug3[0]))
    if puntos_jug4[0]<=0:
        print("El {} con {} ha ganado\n".format(jug4,puntos_jug4[0]))
else:
#Ronda2
    print("Ronda 2:\n")
    puntos_jug1.append(puntos_jug1[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug1))))
    puntos_jug1[1] = puntos_jug1[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug1)))
    puntos_jug1[1] = puntos_jug1[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug1)))
    puntos_jug2.append(puntos_jug2[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug2))))
    puntos_jug2[1] = puntos_jug2[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug2)))
    puntos_jug2[1] = puntos_jug2[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug2)))
    puntos_jug3.append(puntos_jug3[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug3))))
    puntos_jug3[1] = puntos_jug3[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug3)))
    puntos_jug3[1] = puntos_jug3[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug3)))
    puntos_jug4.append(puntos_jug4[0] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug4))))
    puntos_jug4[1] = puntos_jug4[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug4)))
    puntos_jug4[1] = puntos_jug4[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug4)))
    if puntos_jug1[1]<=0 or puntos_jug2[1]<=0 or puntos_jug3[1]<=0 or puntos_jug4[1]<=0:
        if puntos_jug1[1]<=0:
            print("El {} con {} ha ganado\n".format(jug1,puntos_jug1[1]))
        if puntos_jug2[1]<=0:
            print("El {} con {} ha ganado\n".format(jug2,puntos_jug2[1]))
        if puntos_jug3[1]<=0:
            print("El {} con {} ha ganado\n".format(jug3,puntos_jug3[1]))
        if puntos_jug4[1]<=0:
            print("El {} con {} ha ganado\n".format(jug4,puntos_jug4[1]))
    else:
#Ronda3
        print("Ronda 3:\n")
        puntos_jug1.append(puntos_jug1[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug1))))
        puntos_jug1[2] = puntos_jug1[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug1)))
        puntos_jug1[2] = puntos_jug1[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug1)))
        puntos_jug2.append(puntos_jug2[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug2))))
        puntos_jug2[2] = puntos_jug2[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug2)))
        puntos_jug2[2] = puntos_jug2[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug2)))
        puntos_jug3.append(puntos_jug3[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug3))))
        puntos_jug3[2] = puntos_jug3[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug3)))
        puntos_jug3[2] = puntos_jug3[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug3)))
        puntos_jug4.append(puntos_jug4[1] - int(input("Introduce el valor del {} del {}:\n".format("dardo1",jug4))))
        puntos_jug4[2] = puntos_jug4[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo2",jug4)))
        puntos_jug4[2] = puntos_jug4[2] - int(input("Introduce el valor del {} del {}:\n".format("dardo3",jug4)))
        if puntos_jug1[2]<=0 or puntos_jug2[2]<=0 or puntos_jug3[2]<=0 or puntos_jug4[2]<=0:
            if puntos_jug1[2]<=0:
                print("El {} con {} ha ganado\n".format(jug1,puntos_jug1[2]))
            if puntos_jug2[2]<=0:
                print("El {} con {} ha ganado\n".format(jug2,puntos_jug2[2]))
            if puntos_jug3[2]<=0:
                print("El {} con {} ha ganado\n".format(jug3,puntos_jug3[2]))
            if puntos_jug4[2]<=0:
                print("El {} con {} ha ganado\n".format(jug4,puntos_jug4[2]))
        else:
            print("El {} termina las 3 rondas con {} puntos\n".format(jug1,puntos_jug1[2]))
            print("El {} termina las 3 rondas con {} puntos\n".format(jug2,puntos_jug2[2]))
            print("El {} termina las 3 rondas con {} puntos\n".format(jug3,puntos_jug3[2]))
            print("El {} termina las 3 rondas con {} puntos\n".format(jug4,puntos_jug4[2]))