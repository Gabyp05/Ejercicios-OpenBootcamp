from pickle import *

class Vehiculo:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        
    def __str__(self):
        return self.color + " " + self.puertas


cruz = Vehiculo("Negro", "4")
print(cruz)

f = open('vehiculo', 'w+b')

dump(cruz, f)

f.seek(0)
nuevo_cruz = load(f)

print(nuevo_cruz)
f.close()
