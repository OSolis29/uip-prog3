import os
print ("Quiz 5")
print ("lista de supermercado \n ")
l1 = []
c = 0
while c == 0:
        print ("Escoja una de las siguientes opciones")
        print ("1: si desea agregar algo a la lista")
        print ("2: si desea editar ")
        print ("3: si desea eliminar ")
        r = input("4: si desea ver la lista completa \n\n")
        if r == "1":
                a = input("introduzca el nombre del nuevo objeto de la lista\n")
                l1.append(a)
        elif r == "2":
                i = int(input("introduzca la pocision del objeto a editar\n "))
                l1[i] = input("ahora introduzca el nuevo nombre del objeto\n")          
        elif (r == "3"):
                i = input("introduzca la pocision del objeto a eliminar\n ")
                del l1[i]         
        elif (r == "4"):
                print (l1)

        

        
