diameter=int(input("Enter diameter : "))
def vol(dia):
    vol = 4/3*3.14*pow(dia,3)/8
    return vol
volume = vol(diameter)
print(volume)
