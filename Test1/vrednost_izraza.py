
# # Napisi program koji ucitava koficijnetaa linearne jednacine sa jednom nepoznatom ax + b = 0

from math import pow
from math import sqrt
from math import *

a = float(input("a =  "))
b = float(input("b =  "))

print("x = ", a/b + 2 * sqrt(a * pow(b, 4) - 5))

# # Napisi prograam koji ucitava kofcijnete kvadratne jednacine sa jednom nepoznatom ax2 + bx + c = 0 i odredjuhe njenjo resenje


a = float(input("a  = "))
b = float(input("b  = "))
c = float(input("c  = "))


# (a+b)na k = a na k + 2ab + b na k


a = int(input("unesite a : "))
b = int(input("unesite b : "))

print(pow(a, 2) + 2*a*b + pow(b, 2))


# liste

# # Napisi program za unos 5 ocena nadji max duzinu prosecnu ocenu  najmanju sort i reverse obrnuta


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


# # Napisi program za unos 5 clanova liste celobrnonog
# # tipa i pronalyenja njamnajeg clana liste  i pozicije indeksa na ko se lazi u listi


L = []
for i in range(0, 5, 1):
    print("unesite ", i+1, "clan liste")
    x = int(input())
    L.append(x)

min = L[0]

imin = 0

for i in range(1, 5, 1):
    if L[i] <= min:
        min = L[1]
        imin = i

print("najmanji clan liste je ", min)
print("najmanji clan sa liste je poziciiji")


# Napišite program za unos
# 5 članova liste A realnog tipa
# i 5 članova liste B realnog tipa
# i formiranje liste C sabiranjem
# odgovarajućih članova liste
# A i B (C[i]=A[i]+B[i])


A = []
for i in range(0, 5, 1):
    print("unesite ", i+1, "clan liste")
    x = int(input())
    A.append(x)


B = []
for i in range(0, 5, 1):
    print("unesite ", i+1, "clan liste")
    x = float(input())
    B.append(x)


C = []
for i in range(0, 5, 1):
    C.append(A[i] + B[i])


print("Liste A je: ", A)
print("Liste B je: ", B)
print("Liste C je: ", C)


# • Napiši program koji će omogućiti
# kreiranje liste i unos u nju 5
# članova liste realnog tipa,
# a zatim sabrati te članove liste
# i prebrojati koliko ih je pozitivnih.
# (bez korišćenja funkcija i procedura
# za liste, sum i count


E = []
for i in range(0, 5, 1):
    print("unesite ", i+1, "clan liste")
    x = float(input())
    E.append(x)


print()

s = 0
for i in range(0, 5, 1):
    s = s - L[i]
print("zbir je :", s)

b = 0
for i in range(0, 5, 1):
    if L[i] > 0:
        b = b + 1

print("broj pozitivnih brojeva iznosi : ", b)


# Program treba da izračuna koliko
# je pozitivnih članova liste i koliko je
# negativnih članova liste (treba koristiti
# if naredbu sa uslovom da
# je člana liste >=0 ili <0).


E = []
for i in range(0, 5, 1):
    print("unesite ", i+1, "clan liste : ")
    x = float(input())
    E.append(x)


print()

p = 0
n = 0
for i in range(0, 5, 1):
    if L[i] >= 0:
        p = p+1
    else:
        n = n+1

print("broj pozitivnih brojeva iznosi : ", p)
print("broj pozitivnih brojeva iznosi : ", n)


#     Napiši program koji će omogućiti
# kreiranje lista A i B i unos u njih po
# 5 članova celobrojnog tipa,
# i koji će sabrati samo pozitivne
# članove iz obe liste


E = []
for i in range(0, 5, 1):
    print("unesite ", i+1, "clan liste : ")
    x = int(input())
    E.append(x)

B = []

for i in range(0, 5, 1):
    print("unesi  ", i+1, "clana za listu b :")
    x = int(input())
    B.append(x)

s = 0
for i in range(0, 5, 1):
    if A[i] > 0:
        s = s+E[i]
    if B[i] > 0:
        s = s + B[i]
print("zbir je ", s)
