# Este programa tendrás las funciones necesarias para generar las operaciones
# que se le pedirá al jugador que calcule
# Primero importaremos los módulos necesarios
"""
    El módulo random: Necesario para generar las operaciones a calcular de
    manera aleatoria
    Se usará la función:
        randint() que genera aleatorios enteros en un rango determinado
        Esto permitirá generar los números para las operaciones a resolver por
        el jugador
    El módulo os: necesario para actualizar el archivo de registro del Score de
     los jugadores
        Usaremos las funciones remove() y raname()
"""
from os import remove, rename
from random import randint  # ambos forma el ejercicio 1 del libro guía

"""
La siguiente parte del código servirá para almacenar el puntaje de los jugadores
usaremos nombres en inglés por ser algo más cortos
"""


# Se define la función para obtener los puntos del jugador


def getuserscore(username):
    try:
        scores = open("userScores.txt", "r")
        for line in scores:
            listaUser = line.split(",")
            if listaUser[0] == username:
                scores.close()
                return listaUser[1]
        scores.close()
        return "-1"
    except IOError:
        print("\nArchivo userScores.txt no se encontró. "
              "Un nuevo archivo será creado")
        scores = open("userScores.txt", "w")
        scores.close()
        return "-1"


# Se define la función para actualizar el puntaje del jugador
def upadateuserscore(newUser, username, score):
    if newUser:
        scores = open("userScores.txt", "a")
        scores.write("\n" + username + "," + str(score))
        scores.close()
    else:
        scores = open("userScores.txt", "r")
        scorestmp = open("userScores.tmp", "w")
        for line in scores:
            listaUser = line.split(",")
            if listaUser[0] == username:
                line = username + "," + str(score) + "\n"
            scorestmp.write(line)
        scores.close()
        scorestmp.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")


# Ahora hay que generar la operación que el usuario debe resolve
# Se van a requerir dos listas y un diccionario
"""
operandList = es la lista de los números que forman la operación que
                Esta lista tendrá 5 números con 0 como sus valores iniciales
operatorList = es la lista cono los operadores
                debe almacenar 4 cadenas (strings) con "" como sus valores
                iniciales
operatorDict = consiste de 4 pares
                Con enteros del 1 al 4 como las llaves
                y "+", "-", "*", "**"
"""


def generatequestions():
    operandList = [0, 0, 0, 0, 0]
    operatorList = ["", "", "", ""]
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "/", 5: "**"}
    questionString = ""
    while True:
        for i in range(len(operandList)):
            operandList[i] = randint(1, 9)

        operatorAnterior = ""
        for i in range(len(operatorList)):
            operatorList[i] = operatorDict[randint(1, 5)]
            if operatorList[i] == "**" and operatorAnterior == "**":
                operatorList[i] = operatorDict[randint(1, 4)]
                operatorAnterior = operatorList[i]

        # ahora hay que generar la expresión matemática
        openBracket = randint(0, 3)
        closeBracket = randint(openBracket + 1, 4)
        for i in range(0, 5):
            if i == 0:
                if openBracket == 0:
                    questionString = "(" + str(operandList[i])
                else:
                    questionString = str(operandList[i])
            else:
                if i == openBracket:
                    questionString = (questionString + operatorList[i - 1] +
                                      "(" + str(operandList[i]))
                elif i == closeBracket:
                    questionString = (questionString + operatorList[i - 1] +
                                      str(operandList[i]) + ")")
                else:
                    questionString = (questionString + operatorList[i - 1] +
                                      str(operandList[i]))

        newResult = round(eval(questionString), 2)
        if newResult >= -50000 and newResult <= 50000:
            # print(newResult) # solo para pruebas
            break
        # print(newResult) # solo para pruebas
    questionString = questionString.replace("**", "^")

    print("\n" + questionString)
    respuesta = input(
        "Por favor ingrese su respuesta (redondeado a 2 decimales) ")
    while True:
        try:
            if float(respuesta) == newResult:
                print("\n" + "¡Respuesta correcta!, ha ganado un punto")
                return 1
            else:
                print("\n" + "Respuesta incorrecta, la respuesta correcta es ",
                      newResult)
                return 0
        except Exception as e:
            print("Usted no ingresó un número, por favor intente otra vez", e)
            respuesta = input("Por favor ingrese su respuesta ")
