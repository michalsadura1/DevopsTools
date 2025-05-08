#!/usr/bin/env python3
# Function
def function_name():
    print("First function")
    return 0
function_name()

# function with argumnet

def function_name(x=0):
    print("First function")
    if x==1:
        return 1
    return 0

x=function_name()
y=function_name(1)
print(x,y)
