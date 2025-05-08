#!/usr/bin/env python3

# list
numbers = [1,2,3,4]
print(numbers)
# empty list
empty = []
print(empty)

notempty = [1, 2, "Andzej23", "Tadzin" ]
print(notempty[3])

languages = ["Python", "Go", "php", "sql", "terraform", "ansible" ]
print(languages[1])

#slice
napis=["P", "y", "t", "h", "o", "n"," ","j", "e", "s", "t", " ", "S", "u", "p", "e", "r"]
print(napis[0:6])
print(napis[7:11])
print(napis[12:18])
print(napis[:])
print(napis[:6])
print(napis[12:])

# extend list on naother list
list1 = [1,2,3]
list2 = [4,5,6]

print("Lista1: ", list1)
print("Lista2: ", list2)

list1.extend(list2)
print("List1: ", list1)

#Update list elemnts
notempty[3] = "Andrzej24"
print(notempty)

# del list elemts
del languages [-1]
print(languages)

# emove method
languages.remove("terraform")
print(languages)

# method insert
languages.insert(-1,"C++")
print(languages)

# clear list
languages.clear()
print(languages)



# method index check on which index exist sepcyfic value
languages = ["Python", "Go", "php", "sql", "terraform", "ansible" ]
x=languages.index("Go")
print(x)

# reverse
languages.reverse()
print(languages)

################
#TUPLE##########
################


tuple = (1,2,3)
print(tuple)

tuple = (1, "Michal", 2.4)
print(tuple)


tuple = ((1 ,2, 3),["Tomek", "Jolka", "Tadzin"],7,8,9)
print(tuple)

# tuple declaration
var1 = ("Tuple")
var2 = ("Tuple", )

print(type(var1))
print(type(var2))

print(var1)
print(var2)

#######
# Dict
#######
numbers = {1:"one", 2: "two", 3:"three"}
print(numbers)
numbers[4] = "four"
numbers[5] = "five"
print(numbers)
numbers[5] = "FIFEV"
print(numbers)


