### Ciklusok és elágazások gyakorlása

# 1) feladat:

"""
Írd ki a páros és páratlan számokat 1-100 között, külön kategorizálva!
P.:
Páros számok: 2, 4, 6, ...
Páratlan számok: 1, 3, 5, ...
"""

print("Páros számok: ")
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")
    
print("\nPáratlan számok: ")
for i in range(1,101):
    if i%2!=0:
        print(i, end=" ")

print()
# 2. feladat:

"""
Írj programot amely kiírja a számokat 1-10 között, vesszővel elválasztva, de az 
utolsó szám után már ne kerüljön vessző.
"""

for i in range(1,11):
    if i<10:
        print(i, end=", ")
    else:
        print(i)


# 3. feladat:

"""
Írj programot amely eldönti egy beolvasott szám helyességét! Akkor helyes az input, ha
a szám 1500-2700 között van és osztható 7-tel, valamint az 5 többszöröse. Írjuk ki, hogy
a helyes vagy helytelen volt-e az input.
"""

x = int(input("Szám: "))
if (x>=1500 and x<=2700) and (not x%7 and not x%5):
    print("A beolvasott szám megfelel a követelményeknek!")
else:
    print("A beolvasott szám nem felel meg a követelményeknek!")

# Írd át a fenti programot, hogy rossz input esetén kérje újra a számot, mindaddig
# amíg helyes nem lesz!

x = int(input("Szám: "))
while not((x>=1500 and x<=2700) and ( x%7==0 and x%5==0)):
    print("A beolvasott szám nem felel meg a követelményeknek!")
    print("Kérlek add meg újra: ")
    x = int(input("Szám: "))
else: # nem kötelező else-t használni, lehet nélküle is
    print("A beolvasott szám megfelel a követelményeknek!")


# 4. feladat:

"""
Készíts programot, amely kirajzolja az alábbi alakzatot:
*
**
***
****
*****
****
***
**
*
"""
n=5
for i in range(n): # ez a háromszög teteje
    for j in range(i):
        print("*", end="")
    print('')
# a háromszög alsó része
for i in range(n,0,-1): # n-től 0-ig, visszafelé számolva
    for j in range(i):
        print("*", end="")
    print('')


# 5. feladat

# Rajzolj ki egy X-et csillagokból!

n=9
for i in range(n):
    for j in range(n):
        if j==i or j==n-i:
            print("*", end='')
        else:
            print(' ', end='')
    print()