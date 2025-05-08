#!/usr/bin/env python3

# Exmaple dictionray
dict = {"Piotr":30, "Pawel":40, "Radek":29}
print(dict)

# new elemnet
dict["kasia"]=29
print(dict)

#nested dict
dict["Bulka"]={"tes1": 12, "test2": 13 }
print(dict)

# display keys
x=dict.keys()
print(x)


# delete last element display value
x=dict.pop("Bulka")
print(x)

# display items
x=dict.values()
print(x)