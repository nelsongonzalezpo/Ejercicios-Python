#Ejercicio 5

#Diferentes tipos de variable y formas de imprimir

name = "Will Smith"
age = 46
height = 179 #cm
weight = 177 #lb
address = "Elm Street, no. 666"
eyeColor = "Azuk"
status = "Alive"

print "Me llamo %s y tengo los ojos de color %s" %(name, eyeColor)
print "Tengo %d anios, peso %d libras y mido %d centimetros " %(age, weight, height)
print "Vivo en %s " %address

if(status != "Dead"):
    print "Aun estoy vivo"

else:
    print "Estoy muerto"
