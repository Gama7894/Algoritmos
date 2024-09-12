def binary_search(a, low, high, key):
   mid = (low + high) // 2
   if (low <= high):
      if(a[mid] == key):
         print("The element is present at index:", mid)
      elif(key < a[mid]):
         binary_search(a, low, mid-1, key)
      elif (a[mid] < key):
         binary_search(a, mid+1, high, key)
   if(low > high):
      print("Unsuccessful Search")

def Opciones():
   print("\n1.Agregar a la lista\n2.Eliminar\n3.Imprimir\n4.Busacar\n5.Salir\n")

def imprimirlista(lista):
	for item in lista:
		print(item)

a = [6, 12, 14, 18, 22, 39, 55, 182]
n = len(a)    
low = 0
high = n-1

while True:
    Opciones()
    opciones = int(input("Que accion desea hacer?"))
    if opciones == 1:
        Nuevo = int(input("Que numero desea agregar?"))
        if Nuevo in a:
            print("Este elemento ya existe")
        else:
            a.append(Nuevo)
            a.sort()

    elif opciones == 2:
       Eliminar = int(input("Que numero desea eliminar?"))
       if Eliminar in a:
        a.remove(Eliminar)
        a.sort()
       else:
           print("Eeste elemento no existe") 

    elif opciones == 3:
       imprimirlista(a)

    elif opciones == 4:
        a.sort()
        key = int(input("Que numero desea buscar?"))
        binary_search(a, low, high, key)
        key = int(input("Que numero desea buscar?"))
        binary_search(a, low, high, key)

    elif opciones == 5:
        break
