#Separar por letras

palabra = ""

palabra = raw_input("Ingrese una palabra: ")

for letra in palabra:
    print letra

#Separar por letras y voltear

reverse = ""
nuevaPalabra = ""

nuevaPalabra = raw_input("Ingrese una palabra: ")
#Ciclo para voltear
for letra in nuevaPalabra:
    reverse = letra + reverse

#Ciclo para imprimir
for letra in reverse:
    print letra
