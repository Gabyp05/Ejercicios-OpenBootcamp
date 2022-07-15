class Alumno:
    def ingresar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def resultado(self):
        if self.nota > 10:
            print("Aprobado")
        else:
            print("Reprobado")

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.ingresar("Gabriela",18)
alumno2.ingresar("Richard", 9)

alumno1.mostrar_datos()
alumno1.resultado()
alumno2.mostrar_datos()
alumno2.resultado()
