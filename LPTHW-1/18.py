#Ejercicio 18

def print_two(*args):
    one = raw_input("Give one ")
    two = raw_input("Give two ")
    print "Funcion imprimir ambos"
    print one, two


def print_none():
    print "Funcion print none"
    print "na-da"

def print_saludo():
    nombre = raw_input("Como te llamas?")
    print "Hola %s" %nombre


print_two()
print_none()
print ""
print_saludo()
