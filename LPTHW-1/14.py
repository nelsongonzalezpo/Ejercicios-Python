#Ejercicio 14

from sys import argv

script, user_name = argv

prompt = ">"

print "Hi %s, I am the %s script" %(user_name, script)

print "Give random number %s" %user_name
number = raw_input(prompt)

print "%s you have selected this number %r" %(user_name, number)
