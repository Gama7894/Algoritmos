#sumar o restar los numeros de un vector
#preguntar la longitud del vector
#Llenar con numeros random(0-9)
#preguntar operacion
#imprimir vector y resultado

import numpy as np
import random as r

Vector = []
Lista = []
Operacion = input("Que operacion quiere realizar? ")
longitud = int(input("Que longitud tendra el vector? "))

for i in range(longitud):
    Lista.append(r.randint(0,9))
Vector = np.array(Lista)

if Operacion == "suma":
    Resultado = sum(Vector)
    print(Resultado)
else:
    Resta = Vector[0]
    for j in range(longitud):
        Resta = Resta - Vector[j]
    print(Resta)

print(Vector)
