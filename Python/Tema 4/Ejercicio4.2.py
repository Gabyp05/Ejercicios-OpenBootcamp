num1 = int(input ("Ingresa un numero: "))
num2 = int(input ("Ingresa un numero: "))
numero_impar: [int] = []

for i in range (num1, num2):
    if(i % 2 != 0):
        numero_impar.append(i)

print(f"Numeros impares entre {num1} y {num2}: ")
print(numero_impar)
