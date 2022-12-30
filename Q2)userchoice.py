rows=int(input("choice"))
if rows==2:
    for i in range(5):
        for j in range(i):
            print(" ",end="")
        for j in range(5-i):
            print("*",end=" ")
        print()
    for i in range(4):
        for j in range(4-i):
            print(" ",end="")
        for j in range(i+2):
            print("_",end=" ")
        print()
elif rows==1:
    for i in range(5):
        for j in range(i):
            print(" ",end="")
        for j in range(5-i):
            print("*",end=" ")
        print()
else:
    print("Invalid Input")