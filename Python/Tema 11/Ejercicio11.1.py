import sqlite3

connection = sqlite3.connect('ejercicio1.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE Alumnos(ID INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Gabriela', 'Patiño')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Richard', 'Patiño')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Eliana', 'Hernandez')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Mathias', 'Gomez')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Carlos', 'Morales')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Aranza', 'Segura')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Aly', 'Velasquez')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Betsi', 'Cruz')")

connection.commit()

cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Mathias'")

filas = cursor.fetchall()

print(filas)
cursor.close()
connection.close()
