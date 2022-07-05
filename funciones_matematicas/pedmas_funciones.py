# Este programa tendrás las funciones necesarias para generar las operaciones
# que se le pedirá al jugador que calcule
# Primero importaremos los módulos necesarios
# El módulo random: Necesario para generar las operaciones a calcular de
# manera aleatoria
# Se usará la función randint() que genera aleatorios enteros en un rango determinado
# Esto permitirá generar los números para las operaciones a resolver por jugador
# El módulo os: necesario para actualizar el archivo de registro del Score de
# los jugadores; usaremos las funciones remove() y raname()

from os import remove, rename
from random import randint  # ambos forma el ejercicio 1 del libro guía

# La siguiente parte del código servirá para almacenar el puntaje de los jugadores
# usaremos nombres en inglés por ser algo más cortos
# Se define la función para obtener los puntos del jugador


def getuser_score(username):
    try:
        scores = open("userScores.txt", "r", encoding="utf-8")
        for line in scores:
            lista_user = line.split(",")
            if lista_user[0] == username:
                scores.close()
                return lista_user[1]
        scores.close()
        return "-1"
    except IOError:
        print("\nArchivo user_scores.txt no se encontró. Un nuevo archivo será creado")
        scores = open("userScores.txt", "w", encoding="utf-8")
        scores.close()
        return "-1"


# Se define la función para actualizar el puntaje del jugador
def upadateuser_score(new_user, username, score):
    if new_user:
        scores = open("userScores.txt", "a", encoding="utf-8")
        scores.write("\n" + username + "," + str(score))
        scores.close()
    else:
        scores = open("userScores.txt", "r", encoding="utf-8")
        scorestmp = open("userScores.tmp", "w", encoding="utf-8")
        for line in scores:
            lista_user = line.split(",")
            if lista_user[0] == username:
                line = username + "," + str(score) + "\n"
            scorestmp.write(line)
        scores.close()
        scorestmp.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")


# Ahora hay que generar la operación que el usuario debe resolve
# Se van a requerir dos listas y un diccionario
# operand_list:
# Es la lista de los números que forman la operación.
# Esta lista tendrá 5 números con 0 como sus valores iniciales
# operator_list:
# Es la lista con los operadores.
# Debe almacenar 4 cadenas (strings) con "" como sus valores iniciales
# operator_dict:
# Consiste de 4 pares con enteros del 1 al 4 como las llaves y "+", "-", "*", "**"
# los valores
def generatequestions():
    operand_list = [0, 0, 0, 0, 0]
    operator_list = ["", "", "", ""]
    operator_dict = {1: "+", 2: "-", 3: "*", 4: "/", 5: "**"}
    question_string = ""
    while True:
        for i, valor in enumerate(operand_list):
            valor = randint(1, 9)
            operand_list[i] = valor

        operator_anterior = ""
        for i, valor in enumerate(operator_list):
            valor = operator_dict[randint(1, 5)]
            operator_list[i] = valor
            if operator_list[i] == "**" and operator_anterior == "**":
                operator_list[i] = operator_dict[randint(1, 4)]
                operator_anterior = operator_list[i]

        # ahora hay que generar la expresión matemática
        open_bracket = randint(0, 3)
        close_bracket = randint(open_bracket + 1, 4)
        for i in range(0, 5):
            if i == 0:
                if open_bracket == 0:
                    question_string = "(" + str(operand_list[i])
                else:
                    question_string = str(operand_list[i])
            else:
                if i == open_bracket:
                    question_string = (
                        question_string
                        + operator_list[i - 1]
                        + "("
                        + str(operand_list[i])
                    )
                elif i == close_bracket:
                    question_string = (
                        question_string
                        + operator_list[i - 1]
                        + str(operand_list[i])
                        + ")"
                    )
                else:
                    question_string = (
                        question_string + operator_list[i - 1] + str(operand_list[i])
                    )

        new_result = round(eval(question_string), 2)
        if -50000 <= new_result <= 50000:
            # print(new_result) # solo para pruebas
            break
        # print(new_result) # solo para pruebas
    question_string = question_string.replace("**", "^")

    print("\n" + question_string)
    respuesta = input("Por favor ingrese su respuesta (redondeado a 2 decimales) ")
    while True:
        try:
            if float(respuesta) == new_result:
                print("\n" + "¡Respuesta correcta!, ha ganado un punto")
                return 1
            else:
                print(
                    "\n" + "Respuesta incorrecta, la respuesta correcta es ", new_result
                )
                return 0
        except ValueError:
            print("Usted no ingresó un número, por favor intente otra vez")
            respuesta = input("Por favor ingrese su respuesta ")
