#!/usr/bin/env python3

my_list= [1,2,3,4,5]
x=len(my_list)
print(x)
print(type(my_list))
print(my_list)

my_list= [1,2,3,4,5]
x=my_list[len(my_list)-2]
print(x)
#x=my_list[-1]

my_list= [1,2,3,4,5]
# list slice
x=my_list[1:-1]
print(x)

my_list= [1,2,3,4,5]
x=my_list[0:]
print(x)


my_list= [1,2,3,4,5]
x=my_list[2:3]
print(x)

# add last element
my_list= [1,2,3,4,5]
my_list.append("6")
print(my_list)

# remove only one elemnt firt find
my_list.remove("6")
print(my_list)


# remove last element from lits and display value
my_list= [1,2,3,4,5,6,7,8]
x=my_list.pop()
print(x)