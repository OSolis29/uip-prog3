import os

print ("Bienvenido\n")
print ("1.Imprimir numeros de telefono")
print ("2.Agregar numeros de telefono")
print ("3.Quitar numeros de telefono")
print ("4.Buscar numeros de telefono")
print ("5.Salir")

directorio = {}
nombres = directorio.keys()
numeros = directorio.values()
elementos = directorio.items()
var = 0

while var != 6:
        var = int (input ("Escriba un numero entre 1 y 5:  "))
        if var==1:
                for nombres, numeros in elementos:
                        print ("Nombre: ", nombres, "\nNumero:", numeros, "\n")

        elif var == 2:
                print ("agregar nombres y numeros")
                name= input ("Nombre: ")
                num = input ("Numero:")
                directorio [name] = num
        elif var == 3:
                eli=input ("Inserte el nombre a eliminar: ")
                del directorio[eli]
        elif var == 4:
                search = input ("inserte el nombre del contacto \nNombre: ")
                print ("Numero: "+directorio[search])


