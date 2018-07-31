#Ejercicio 8

formatter = "%r%r%r%r"

print formatter %(1,2,3,4)
print formatter %("Hola", "hola", "ola", "0la")
print formatter %(True, False, True, False)
print formatter %(formatter, formatter, formatter, formatter)

print formatter %(
"How",
"Are",
"You",
"?"
)
