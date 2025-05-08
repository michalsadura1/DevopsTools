#!/usr/bin/env python3

# dict
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for number in numbers:
    print(number)

# condition loop

for number in numbers:
    if number % 2 == 0:
        print(number)
        continue

tupel= (21.37, 21.38, 21.39)

# tuple
for item in tupel:
    print(item)

# dict
persons = {"Adam":21, "Ewa":22, "Tadek":76 }
for key in persons:
    print(key)

persons = {"Adam":21, "Ewa":22, "Tadek":76 }
for key, persons in persons.items():
    print(f"Name:{key},age: {persons}")

# lit of tuple
#x,y = 9,0
# print x
# print y

points = [(21,37), (21,38), (21,39)]

for x,y in points:
    print(f"x:{x},y:{y}")