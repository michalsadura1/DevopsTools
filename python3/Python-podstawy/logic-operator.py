#!/usr/bin/env python3

firstname =""
lastname ="Sadura"

print(bool(firstname))
print(bool(lastname))

if firstname or lastname:
    print(f"{firstname} or {lastname}")



firstname2 ="" or "Janek"
lastname2 ="Sadura" or ""

print(bool(firstname2))
print(bool(lastname2))

if firstname2 or lastname2:
    print(f"{firstname2} or {lastname2}")