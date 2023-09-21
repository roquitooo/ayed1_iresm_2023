"""El programa debe:

Preguntar al usuario por una frase y una letra
mostrar por pantalla el número de veces que aparece la letra en la frase."""

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

cont = 0
for i in frase:
    if i == (letra):
        cont +=1
print (f"la cantidad de veces que aparece la letra: {letra} en la frase es: ", cont)
