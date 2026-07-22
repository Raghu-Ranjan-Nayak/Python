#Serch for a number x in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100)
x = 81
i = 0
while i < len(tuple):
    if(tuple[i] == x):
        print("x is found at index",i)
    i += 1
