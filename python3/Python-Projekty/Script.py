#!/usr/bin/env python3

def gather_info():
    haight=  float(input("Podaj swoj wzrost(cale lub metry): " ))
    weight=  float(input("Podaj swoja wage(funty kilogramy): " ))
    system=  input("Jaki system (imperialny / metryczny):  ").lower().strip()
    return( haight, weight, system)

def calculate_bmi(haight, weight, system="metryczny"):
    if system == "metryczny":
        bmi=(weight/(haight**2))
    else:
        bmi= 703 * (weight/(haight**2))
    return(bmi)

while True:
    haight, weight, system = gather_info()
    if system.startswith("i"):
        bmi = calculate_bmi(haight=haight, weight=weight, system=system)
        print(f"Twoje BMI to: {bmi}")
        break
    elif system.startswith("m"):
        bmi = calculate_bmi(haight=haight, weight=weight, system=system)
        print(f"Twoje BMI to: {bmi}")
        break
    else:
        print("-------------------------------","Error wpisano zly system","Powinien byc (imperialny / metryczny)","-------------------------------", sep="\n")
