list_a=[1,2,3,4,5]
try:
    i = int(input("Enter The Index:"))
    print(list_a[i])
except ValueError:
    print("Use an Integer value as the input")
except IndexError:
    print("The index",i,"is incorrect and index should lie between -5 and 4")
