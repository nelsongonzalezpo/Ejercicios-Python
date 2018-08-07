#Ejercicio 36

#Designing and debugging

print "Escribe la palabra 'Jorge'"

name = raw_input(">")

if name == "Jorge":
    print "Muy bien, lo lograste"

elif name == "jorge":
    print "Casi lo logras, te falto la 'J'"

else:
    print "Fallaste el intento"

i = 0

while i < 6:
    print i, " el nombre es ", name, " tenia que ser Jorge "
    i = i+1
