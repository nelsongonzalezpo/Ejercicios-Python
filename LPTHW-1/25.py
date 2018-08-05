def break_words(stuff):
    words = stuff.split(" ")
    return words

def sort_words(words):
    return sorted(words)

print "Vamos a separar las palabras"
print break_words("Hola Como Estas")
print "Vamos a separar las letras"
print sort_words("Hola Como Estas")
