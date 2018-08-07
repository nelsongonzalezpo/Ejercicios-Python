#Ejercicio 30

people = 30
cars = 40
buses = 15

if cars > people:
    print "Debemos irnos en carro"

elif people > cars:
    print "Debemos caminar o en camion"

else:
    print "Apenas dan los carros"

if  people < buses:
    print "Debemos ir en autobus"

elif people > buses:
    print "Tal vez no alcance"

buses += 15

if people == buses:
    print "Que coincidencia"
