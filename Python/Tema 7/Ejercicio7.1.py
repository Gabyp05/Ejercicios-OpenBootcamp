from operadores import * 

num1 = int(input("Ingresa primer número: "))
num2 = int(input("Ingresa segundo número: "))

print("""
    1) Sumar       3) Multiplicar
    2) Restar      4) Dividir
    """)

opcion=input("Ingresa el número de la operación que deseas realizar: ")

if opcion=="1":
    print( "{} + {} = {}".format(num1, num2, suma(num1, num2)))
elif opcion=="2":
    print( "{} - {} = {}".format(num1, num2, resta(num1, num2)))
elif opcion=="3":
    print( "{} * {} = {}".format(num1, num2, multiplicacion(num1, num2)))
elif opcion=="4":
    print( "{} / {} = {}".format(num1, num2, division(num1, num2)))
else:
    print("Opción no válida")
