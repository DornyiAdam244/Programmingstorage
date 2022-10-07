# Sztringek haladó 

s1 = "Csodás péntek reggel van."
print(s1)

#Szeletelés: 
print(s1[0])# A sztring első betűje :
print(s1[0:5]) # A sztring első 5 betűje 
print(s1[:6]) # A sztring első 6 betűje
print(s1[2:8]) # 3-tól 7-ig
print(s1[7:]) # 7-től a végéig
print(s1[-1]) # Az utolsó betű
print(s1[-1:-5:-1]) # az utolsó 4 betű visszafelé
print(s1[-5]) # az utolsó 4 betű
# sztring megfordítása:
print(s1[::-1])

# Karakter csere

#s1[0]="A" Ez nem jó, nem engedélyezett!! Helyette replace() methódus:
s1.replace(" ", "*")
s2=s1.replace(" ", "*")
print(s2)
print(s1.replace("C", "A"))

# Minden második betű kiírása:
abc="abcdefghijklnmopqrstuvwxy"
print(abc[::2])


# Egy adott rész megkeresése a sztringben: find() methódussal
print(abc.find("k"))

# Sztringek összefűzése:
sz1="Ez"
sz2="egy"
sz3="összefűzés"
sz4="Pythonban"
sz5="!"
print (sz1+" "+sz2+" "+sz3+" "+sz4+sz5)

# Sztring bejárása for ciklussal:

abc="abcdefghijklnmopqrstuvwxy"
for c in abc: 
    print(c)
    # Ilyenkor a ciklus változó a sztring adott elemének az értéket kapja meg (nem számlál)



"""
Írj egy programot amely bekér két darab 3 karakteres sztringet, majd összefűzi azokat, oly módon, hogy
a középső karaktereket kicseréli a két sztringben.
"""

s1 = str(input("Kérem az első sztringet! "))
s2 = str(input("Kérem az első sztringet! "))
print(s1.replace(s1[1],s2[1])+" "+s2.replace(s2[1], s1[1]))


# További sztring methódusok:

print(abc.capitalize()) # Nagy kezdő betűs sztring

