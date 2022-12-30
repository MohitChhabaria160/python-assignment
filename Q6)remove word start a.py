list_a = ["car", "place", "tree", "under", "grass", "price"]
z=[]
flag=False
for i in list_a:
    if "a" in i:
        continue
    else:
        z.append(i)
print(z)
