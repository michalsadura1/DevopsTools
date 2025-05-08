#!/usr/bin/env python3
# path to file
import os
cwd = os.getcwd()
print(cwd)
persons="./persons.txt"

print(persons)
text_file=open(persons,'r')
print(text_file.read())
# seek powrot do 1 pozycji listy
print(text_file.seek(0))
text_file.seek(0)
print(text_file.read())
text_file.seek(0) 

for line in text_file:

    print(line, end="\n")
text_file.close()


text_file=open(persons,'r')
print(text_file.read())
text_file.seek(0)
#text_file.close()
# write to new file

persons2="./persons2.txt"
text_file2=open( persons2,'w')
text_file2.write(text_file.read())
text_file2.write("\n")
text_file.close()

text_file2=open( persons,'r')
print(text_file2.read())
text_file2.seek(0)
text_file2.close()


# with open and close

with open("./persons2.txt", 'a') as f:
    f.write("Koniec") 