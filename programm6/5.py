import math

def масса_воды_в_цилиндре(radius, height):
    volume = math.pi * (radius ** 2) * height 
    density_of_water = 1000 
    mass = volume * density_of_water  
    return round(mass, 2)

radius = 0.5 
height = 1.0  
print(масса_воды_в_цилиндре(radius, height)) 