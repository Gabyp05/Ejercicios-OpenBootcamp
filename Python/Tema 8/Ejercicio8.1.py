f = open('prueba.txt','w')
f.write('Hola, es una prueba \n')
f.close()

f = open('prueba.txt', 'r+')
f.readline()
f.write('Esto seria otra linea.\n')

f.seek(0)
print(f.read())
f.close()
