palabra = "Hola Mundo"
print palabra

nombre1 = "Juan"
nombre2 = "Maria"

print "Hola %s" %nombre1
print "Hola %s" %nombre2


#Funcion para saludar
def saludar(nombre):
    print "Saludando a", nombre

saludar(nombre1)

#Arreglo de nombres
arreglo = [nombre1, nombre2]

for nombres in arreglo:
    print "Imprimiendo arreglo con valor ", nombres
