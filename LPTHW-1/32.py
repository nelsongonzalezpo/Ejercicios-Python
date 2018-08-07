#Ejercicio 32

the_count = [1,2,3,4]
fruits = ["apples", "oranges", "pears"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
    print "El numero %d" %number

for fruit in fruits:
    print "La fruta %s" %fruit

for element in change:
    print "The element %r" %element

elements = []

for i in range(0,6):
    print "Adding %d to the list" %i
    elements.append(i)

for i in elements:
    print "Element was:%d" %i
