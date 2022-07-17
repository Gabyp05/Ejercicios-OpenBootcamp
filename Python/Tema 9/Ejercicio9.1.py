lista = input("Ingresa nombres de países separados por comas: \n")

paises = [pais for pais in lista.split(",")]

print(",".join(sorted(list(set(paises)))))
