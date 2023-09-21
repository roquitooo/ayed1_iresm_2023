try:
    palabra = input("Escribe una palabra: ")
    
    if palabra.isalpha():
        for letra in palabra:
            print(letra)
    else:
        print("No ingresaste una palabra válida.")
except Exception as e:
    print(e)