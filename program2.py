i = 2.54
a = float(input("Enter inches: "))
while a >= 0:
    total = i*a
    print(total)
    a = float(input("Another value of inches or enter negetive number to exit: "))
else:
    print("Exit program")