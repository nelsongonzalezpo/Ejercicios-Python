#Ejerccio 39

print "Wait theres not 10 things in that list, lets fix that"

ten_things = "Apples Oranges Grapes Light"
stuff = ten_things.split(' ')

more_stuff = ["Hi", "Day", "Night", "Sun", "Spirit", "Fire", "Cold"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "Theres %d items now" %len(stuff)

print "There we go:", stuff
print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
