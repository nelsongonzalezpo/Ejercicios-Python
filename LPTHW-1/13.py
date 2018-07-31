#Ejercicio 13

#Utilizando archivos e inputs desde la ejecucion

#Ejemplo de ejecucion "python 13.py first 2nd 3rd"

from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is called: ", first
print "Your seond variable is called: ", second
print "Your third variable is called: ", third
