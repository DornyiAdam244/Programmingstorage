# Gyakorlás folytatása

# 1. feladat

# Rajzolj ki a képernyőre egy keretes X-et!

"""
**********
**      **
* *    * *
*  *  *  *
*   **   *
*   **
*
"""
"""
n=int(input("Add meg az alakzat magasságát: "))
for oszlop in range(n):
    for sorok in range(n):
        if oszlop==0 or oszlop==n-1:
            print("*", end='')
        else:
            if sorok==1 or sorok==oszlop or sorok==n-1 or sorok==n-oszlop:
                    print('*' ,  end="")
            else: 
                print('', end="")
    print('')
"""
"""
n=int(input("Add meg az alakzat magasságát: "))
for sorok in range(n+1): # Külső ciklus számolja a sorokat
    for oszlopok in range(n+1): # Belső ciklus számolja az oszlopokat
        if sorok==0 or sorok==n: # Tele csillagozom az első és utolsó sort
            print("*" , end='')
        else: # Máskülönben az összes többi sorban:
            if oszlopok==0 or oszlopok==sorok or oszlopok==n or oszlopok==n-sorok: # Csillagot teszek a megjelölt helyekre
                print("*", end="")
            else:  # az üres helyekre pedig 'space' kerül
                print(' ', end='') # Minden sor végére sortörés kerül
    print('')    
## Házi feladat: mindenki a monogramját Írja ki csillagokkal ábrázolva ékezetek nélkül
"""

# 2. Feladat

# Írj programot amely bekér egy számot, ez a szám lesz a tartomány (range) vége, majd számold meg, 
# hogy ebben a tartományban hány darab páros és páratlan szám volt!


"""
n=int(input("Adj meg egy számot: "))
paros, paratlan = 0,0
for i in range(1, n+1):
    if i%2:
        paratlan+=1
    else: 
        paros+=1
print(" A páros és páratlan számok darabja: %d db és %d db " %(paros, paratlan))

"""
"""
A print függvénynek sok formázási lehetősége van. Lehetőségünk van változókat is megjelentíteni a függvényben
Ilyenkor a változó helyét %~Jellel jelölöm meg, majd a %-jel után írom a változó típusát.
Ez lehet: 
%d - decimális szám 
%s - sztring
stb..... (számunkra ez a kettő a lényeges)
A "sztringem" után szintén %-jellem sorolom fel a változó(ka)t
Ha több változó van akkor kötelezően ()-be teszem(sorolom fel).
"""

# 3. Feladat:

# Írj programot, amely bekér egy szöveget a felhasználótól és megfordítja azt!
# pl. Alma-amla


sztring=input("Adj meg egy szöveget: ") # s = sztring
print("A sztring: %s" %sztring)
# Újdonság: a sztring hosszát le tudom kérdezni egy len() függvénnyel, ő egy számot ad vissza 
# Kérdezzük le a begépelt sztring hosszát:
print(len(sztring))
for kar in range(len(sztring)-1,-1,-1):
    print(sztring[kar], end="")
print("\n")
