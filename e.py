"""*   Simular un cajero automatico y pedir usuario y contraseña (user, 1234) 
caso verdadero mostrar menu y en caso falso seguir pidiendo.
*   En caso de mal ingreso de usuario o contraseña 3 veces el programa debe detenerse
"""

usuario = "user"
contrasenia = "1234"

def user_autentication():
    for i in range(3):
        user = input("Ingrese su usuario: ")
        contra = input("Ingrese su contraseña: ")
        if usuario == user and contra == contrasenia:
            print ("Ingresaste al Banco.")
            return True
        else:
            print(f"Ingresaste mal tus datos, te quedan {2-i} intentos de ingreso")
        # si salgo del for es porque agote mis 3 intentos
    return False
    
user_autentication()

