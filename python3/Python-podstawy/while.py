#!/usr/bin/env python3

# loop1 basic one
def loop1():

    hit = 1
    while hit <= 100:
        print(" i am  infinite LooP  almoust ;]")
        print(hit)
        hit += 1

# exceute  function1 loop1() 
# loop1()

# Advanced condition loop
# 
def loop2():

    hit2 = 1
    while hit2 <= 100:
        if hit2 % 2 == 0:
            hit2 +=1
            continue
        print(f"Liczba  nie parzysta: {hit2}")
        hit2+=1

loop2()