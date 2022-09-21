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

x = int(input("Adj meg egy számot: ")) #Típuskényszerítem egész számmá
y = int(input('Adj meg egy másik számot: '))
print(x+=y)
print(x-=y)