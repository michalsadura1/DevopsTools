#!/usr/bin/env python3

# list without modification
my_list=[2.1, 3.7, 2.0, 2.5]
my_tuple=(2.1, 3.7)
print(my_tuple)

#1,2,3,4 == my_list
print(my_list)

my_newtuple=my_tuple + (2.6,)
print(my_newtuple)



w,x,y,z, = my_list
print(w)

w,x = my_tuple
print(x)
