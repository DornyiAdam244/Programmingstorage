### Elágazások folytatás

## Egymásba ágyazott elágazások:

# Írj egy programot, ami megvizsgálja a beolvasott számot, hogy >-e mint 10, és ha igen, akkor vizsgálja meg 
# azt is, hogy >-e mint 20. Ha nagyobb mint 20, akkor írja ki ezt a szöveget, ha nem > mint 20, akkor írja csak ki,
# hogy > mint 10. Ha
#  Ha egyik sem teljesült, akkor írja ki, hogy rossz input!
 

"""
x = int(input('Adj egy 10-nél nagyobb számot: '))
if x > 10:
    if x > 20:
        print(" A szám nagyobb mint 20!")
    else:
        print("A szám nagyobb mint 10, de kisebb mint 20!")
else:
    print('Rossz input!')
"""


###  Ciklusok

## Elöltesztelő ciklus: while


"""
while feltétel teljesül 
    parancsok végrehajtása
"""

# Írj programot ami megvizsgálja a beolvasott inputot, és helyes input esetén kiírja hogy Helyes input,
# rossz input esetén figyelmeztet és újra bekéri az input adatot. Feltétel:
# ha az input < 10, akkor helyes ha >=10, akkor rossz input.

"""
x = int(input('Adj meg egy 10-nél kisebb számot: '))
while x >=10:
    print('Rossz input! ')
    x = int(input('Adj meg egy 10-nél kisebb számot: '))
print("Helyes input! ")
"""

## A ciklus megszakítása:

# Olvass be egy n számot majd írd ki a számokat 1-től n-ig azonban szakítsd meg a ciklust ha n>5-nél és
# elérted az 5-öt.

"""
n = int(input("Adj meg egy számot: "))
i = 1 
while i < n:
    print(i)
    if i == 5:
        break # break megszakít minden folyamatot, kilép a vezérlőszerkezetből.
    i+=1 # Ugyanaz mint i=i+1
"""


## A ciklus folytatása átugrással:
# Olvass be egy n számot majd írd ki a számokat 1-től n-ig úgy hogy kihagyja az 5-öt, amennyiben n>5.
"""
n = int(input("Adj meg egy számot: "))
i = 0 
while i < n:
    i+=1 # Ugyanaz mint i=i+1
    if i == 5:
       continue # Folytatja a vezérlőszerkezetet egy adott feltétel után, úgy hogy visszaugrik 
                # a ciklus elejére. 
    print(i)
"""

## Iteráló ciklus: for

# Írjuk ki a számokat 1-től 10-ig for ciklussal.


for i in range(1,11):
    print(i)

