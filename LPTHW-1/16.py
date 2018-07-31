#jercicio 16

#Choose a different file because the script is going to re-write the file

from sys import argv

script, filename = argv

print "We are going to erase %r" %filename
print "If you dont want that, hit CTRL+C"
print "If you want to proceed, hit RETURN"

raw_input("ANSWER>")

print "Opening file"

#w for writting
target = open(filename, "w")

print "Truncating File..."


line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
