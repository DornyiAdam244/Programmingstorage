#print('Szia uram')
# ez egy comment    
"""
ez
egy 
többsoros 
megjegyzés
"""
#VÁLTOZÓK
""""
- egész számok
- lebegőpontos számok
- sztringek

"""
"""
x = 5
print(type(x))
#Típusát leírja
y = 3.14
print(type(y))
s = "kék az ég"
print(type(s))  

print(x)
print(y)
print(s)
"""
#Változók elnevezésénk szabályai:
"""
- A változó neve mindig kisbetűvel kezd
- A változó neve nem tartalmazhat ékezetes betűt
- A változó neve nem kezdődhet számmal
- A változó neve csak kis- és nagybetűket, valamint számokat és aláhúzás(_)karaktert tartalmazhat
- A változók neve case-sensitive(megkülönbözteti a kis&nagy betűket!!!, betűérzékeny) 
"""

# Néhány példa: 
myvar = "Pista"
my_var = "Pista"
myVar = "Pista"
myVar2 = "Béla"
"""
2myvar = "Béla"
my-var = "Béla"
my var = "Béla"
"""
#ezek mind rosszak


# (Camel Case)
# Több szóból álló változók elnevezése:
# Az első kisbetűvel kezdődik, minden szó pedig nagybetűvel.
# pl.:
ezEgyValtozo = 5


# Minden szó nagybetűvel kezdődi (ezzel megszegem a legfontosabb szabályt,
# nem fog visítani érte a Python, de nem esztétikus.) 
# (Pascal Case)
EzEgyValtozo = 6
#print(EzEgyValtozo, ezEgyValtozo)

# - Minden szót aláhúzás jellel választok el (Snake Case)
# pl.:
ez_egy_valtozo = 5

# Több változó létrehozása, több értékkel, egyszerre: 
# x, y, z = 2,3,4
x = y = z = 5
#print(x, y, z)
"""
 -szöveg (Str)
 -számok (int, float, complex)
 -sorozatos típusok (list, tuple, range)
 -könyvtár (dict)
 -halmaz ()
 -logikai típus
""" 
x = 5 
print(type(x))
y = (float(x))
print(type(y))
y = x
print(type(y))

# Random számok létrehozása:
import random 
print(random.randint(1,100))
# de importálhatom így is:
from random import randint
print(randint(1,100)) 

# Sztringek

print('A sztingeket idézőjelekbe tehetjük, ')
print('Vagy apoztrófok közé is írhatjuk ')
print('''A több soros 
      szövegeket három idézőjel 
      vagy aposztróf közé írjuk.''')
print(''' Vagy
      így''')

# ha idézőjelen belül idézőjelek kell használni, akkor azt / jellel kell :
print("Itt \" jelet kell használnom.")
# ugyanez aposztróffal is
print('Itt \' jelet kell használnom.')

print("Idézőjelen belül ' jelet simán lehet írni.")
print('Aposztrófon belül simán lehet " jelet írni.')

# Bool típusok

# Két féle bool típus létezik: True és False
# Pl.:
print(5<3)
print(10==10)
print(6>=5)

# Operátorok
#Aritmetikai operátorok


"""
Összeadás (+)
Kivonás (-)
Szorzás (*)
Osztás (/)
Maradékos osztás, moduló (%)
Egész osztás (//)
Hatványozás (**)
"""


#Hozzárendelő operátorok:
""" 
Értékesadás (=)
Értékadás összeadással (x+=3 -> x=x+3)
Értékadás összeadással (x+=3 -> x=x-3)
Értékadás szorzással (*=)
Értékadás osztással (/=)
Értékadás maradékososztással (%=)
Értékadás egészosztással (//=)
Értékadás hatványozással (**=)
"""

