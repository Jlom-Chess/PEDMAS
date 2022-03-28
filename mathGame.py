# import FuncionesMatematicas.pedmasFunciones as fm
from FuncionesMatematicas import pedmasFunciones as fm

try:
    username = input("Ingrese su nombre ")
    userScore = int(fm.getuserscore(username))
    if userScore == -1:
        userScore = 0
        newUser = True
    else:
        newUser = False

    print("Bienvenido ", username)
    print("Su puntaje al iniciar el juego es", userScore)
    userChoice = "0"
    while userChoice != "-1":
        score = fm.generatequestions()
        userScore = userScore + score
        print("Puntaje actual", userScore)
        userChoice = input("¿Desea continuar el juego?. Digite -1 para salir ")

    fm.upadateuserscore(newUser, username, userScore)

    print(
        "\n" + "Muchas gracias",
        username,
        "por participar",
        "\n" + "Su nuevo puntaje es",
        userScore,
    )
except Exception as e:
    print("Ha ocurrido un error, lo sentimos", e)
