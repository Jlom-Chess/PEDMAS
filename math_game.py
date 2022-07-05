# import FuncionesMatematicas.pedmasFunciones as fm
from funciones_matematicas import pedmas_funciones as fm


def main():
    try:
        username = input("Ingrese su nombre ")
        user_score = int(fm.getuser_score(username))
        if user_score == -1:
            user_score += 1
            new_user = True
        else:
            new_user = False

        print("Bienvenido ", username)
        print("Su puntaje al iniciar el juego es", user_score)
        user_choice = ""
        while user_choice != "-1":
            score = fm.generatequestions()
            user_score = user_score + score
            print("Puntaje actual", user_score)
            user_choice = input("¿Desea continuar el juego?. Digite -1 para salir ")

        fm.upadateuser_score(new_user, username, user_score)

        print(
            f"\nMuchas gracias {username}, por participar,\nSu nuevo puntaje es "
            f"{user_score}"
        )
    except ValueError:
        print("Ha ocurrido un error, lo sentimos ")


# Programa principal
main()
