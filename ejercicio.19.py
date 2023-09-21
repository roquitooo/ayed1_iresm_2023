"""El programa debe:

Preguntar al usuario una cantidad de dinero a invertir
Preguntar al usuario el interés anual y el número de años
Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

try:
    capital = float(input("Ingrese la cantidad de dinero que quiere invertir: "))
    interes = float(input("Ingrese la cantidad de interes anual: "))
    anios = int(input("Ingrese la cantidad de años que quiere invertir: "))
    ganancia = 0
    for i in range(anios):
        ganancia = (ganancia + capital) * (interes / 100 + 1)
        print (f"Su ganancia en el años {i+1} sera: {ganancia}")
except Exception as e:
    print (e)
