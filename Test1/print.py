

# # Napiši program koji će za unet pozitivan broj da izračuna kvadratni koren i rezultat da zaokruži na dve decimale

import math
a = float(input("unesi neki broj : "))
c = math.sqrt(a)
c = round(c, 2)


print(c)

print(repr(c).rjust(4), end=("  "))

print(repr(c).rjust(4), end=(" | "))
print(repr(c).rjust(4), end=("  "))
