# Operátorok folyt.

# Összehasonlító operátorok:


"""

 
 == - Egyenlőség 
 != - Nem egyenlő
 >  - Nagyobb mint
 <  - Kisebb mint
 >= - Nagyobb vagy egyenlő
 <= - Kisebb vagy egyenlő


"""


# Logikai operátorok:

"""

and - ÉS
or - VAGY
not - NEM


"""

# Identitás operátorok:



"""

is - értéke True ha x is y 
is not - értéke Tue ha x is not y
(azoosságot vizsgál)

"""


# Tagsági operátor


"""

in - valami rész-e a másiknak, értéke True, ha x in y
not in valami nem része a másiknak, értéke True ha x not in y

"""

# Bitműveleti operátorok:

""""

& - bitenkénti ÉS művelet
| - bitenkénti VAGY művelet 
^ - bitenkénti XOR művelet 
~ - bitenkénti NEM művelet 
>> - Jobbra léptetés 
 
 
"""


""""

Írj programot amely, értékadó operátorokkal elvégzi az alapműveleteket két számon. A számokat billentyűzetről olvassuk be!

"""


# Billentyűzetről az input() függvénnyel tudunk adatot beolvasni.
# az input() függvény sztringet olvas be, ezért megfelelő módon
# típuskényszeríteni kell az értékeket. 

"""

x = int(input("Adj meg egy számot: ")) #Típuskényszerítem egész számmá
y = int(input('Adj meg egy másik számot: '))
x+=y # x=x+y
print(x)
x-=y # x=x-y
print(x)
x*=y # x=x*y
print(x)
x//=y # x=x//y
print(x)
x%=y # x=x%y
print(x)
x**=y # x=x**y
print(x) 

"""

### Elágazások (Szelekció) ###



# if ... else:

"""

Ha teljesül a feltétel, akkor végrehajtódik egy parancs,
ha nem teljesül, akkor pedig egy másik parancs hajtódik végre.

"""

# Pl.: Írd ki, hogy Szia Uram! Ha a beolvasott szám nagyobb mint 5!
# Máskülönben írd ki hogy "Rossz input!"

"""

x =int(input("Adj meg egy számot: "))
if x > 5:
    print("Szia uram!")
else:
    print("Rossz input!")

"""

 
# Többszörös elágazás:

# Kérjünk be egy számot a billentyűzetről és vizsgáljuk meg, hogy 
# kisebb, nagyobb, vagy egyenlő-e öttel.

"""

x = int(input("Adj meg egy számot!"))
if x > 5:
    print(str(x)+">5")
elif x < 5:
    print(x+"<5")
else:
    x == 5
    print("x=5")
    
"""

# Elágazások logikai feltétellel:

# Csak akkor írjuk ki a szöveget ha a beolvasott szám
# 5-10 között található

""""

x = int(input("Adj meg egy számot 5-10 között!: "))

if x >= 5 and x <= 10:
   print("Megfelelő input!")
else:
    print("Rossz input!") 


"""

   
# Ha e vagy q gombokat nyomunk lépjen ki a program, egyébként
# jelezzen hibát!

"""

c = input('Adj meg egy karaktert!: ')
if c is 'e' or c is 'q':
    print('Kilép!')
else:
    print('Hiba!')
    
"""

# Rövidített if:

# Ha csak egy sorból áll a feltétel parancsa, akkor írhatjuk így is:

a=5 
b=4
if a>b: print("Az 'a' nagyobb!")

# Rövidített if ... else:
# Ilyenkor először véghajtjuk az if parancsát, majd a vizsgálat után
# jöhet az else

print("Az 'a' nagyobb") if a>b else print('Az a nem nagyobb! ')


# folyt köv...