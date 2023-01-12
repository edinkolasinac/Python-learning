
# # Napisi program koji ucitava koficijnetaa linearne jednacine sa jednom nepoznatom ax + b = 0

# # from math import sqrt
# # from math import *

# # a = float(input("a =  "))
# # b = float(input("b =  "))

# # print("x = ", a/b + 2 * sqrt(a * pow(b, 4) - 5))

# # Napisi prograam koji ucitava kofcijnete kvadratne jednacine sa jednom nepoznatom ax2 + bx + c = 0 i odredjuhe njenjo resenje


# from math import sqrt
# a = float(input("a  = "))
# b = float(input("b  = "))
# c = float(input("c  = "))


# # (a+b)na k = a na k + 2ab + b na k


# from math import pow

# a = int(input("unesite a : "))
# b = int(input("unesite b : "))

# print(pow(a, 2) + 2*a*b + pow(b, 2))


# liste


L = []

for i in range(0, 5, 1):
    print("unesi", i + 1, "ocenu: ")
    x = int(input())
    L.append(x)

print()
print("Najmanja ocena je ", min(L))
print("Najveca ocena je ", max(L))
print("Duzina liste  je ", len(L))
print("Zbire ocena je ", sum(L))

po = sum(L) / len(L)
print("prosecn ocena iznosi : ", po)


L.sort()
print("sortirana lista: ", L)

L.reverse()
print("obrnuta litsa : ", L)
