def numeroprimo():
  numero: int = int(input("Introduce un numero: "))

  if numero > 1:
    for i in range(2,int(numero)):
        if (int(numero) % i) == 0:
            print(f"El numero {numero} NO es PRIMO ")
            break
        else:
            print(f"El numero {numero} SI es PRIMO")
  else:
    print("Debes ingresar un numero mayor a 1")

print(numeroprimo())
