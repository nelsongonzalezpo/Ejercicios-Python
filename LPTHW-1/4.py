#Ejercicio 4

#Ejercicio con declaracion de variables y operaciones

cars = 100
spaceInCar = 5
drivers = cars
spaceTotal = cars * spaceInCar

passengers = (cars * spaceInCar) / 2
carsDriven = cars

spaceLeft = spaceTotal - passengers

print "Hay %d carros disponibles" %cars
print "Hay %d conductores disponibles" %drivers
print "Hay %d espacios para el viaje" %spaceTotal

print "Solo tenemos %d pasajeros" %passengers

if (passengers < spaceTotal):
    print "Hay suficientes espacios, %d para ser exactos" %passengers

elif (passengers > spaceTotal):
    print "No tenemos suficiente espacio en el carro"
