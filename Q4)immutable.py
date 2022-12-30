a=(1,2,3,4)
try:
    a[1]=0
except TypeError:
    print("If we try to change the values in tuple it will rase an error saying('tuple' object does not support item assignment)")

'''In the above example we have observed that if we try to
change the value of the existing tuple we raises an "TypeError" '''


#In my point of view immutability is "when no change is possible over time"
#if the value of an object cannot be changed over time, then it is known as immutable
#Once created, the value of these objects is permanent.
