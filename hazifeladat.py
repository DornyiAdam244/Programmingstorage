for row in range(8):
    for col in range(7):
        if (col==0 or (col==6 and (row!=0) and row!=7)) or ((row==0 or row==7) and (col>0 and col<6)):
            print("*", end="")
        else:
            print(end=" ")
    print(" ")
    
for row in range (7):
	for col in range(5):
		if (row!=0 and col==0) or (row!=0 and col==4) or (row==0 and (col!=0 and col!=4) or (row==3 and (col==1 or col==2 or col==3 or col==4))):
			print("*",end=' ')
		else:
			print(" ",end=" ")
	print()


