esPalin = False

palabra = raw_input()

reversed = ""

for letra in palabra:
    reversed = letra + reversed

if palabra == reversed:
    esPalin = True

else:
    esPalin = False

print esPalin
print palabra
print reversed
