print("My name is Foysal. So Here  I print F : ")

for row in range(7):
    for col in range(5):
        if (col == 0) or ((row == 0 or row == 3) and col > 0):
            print("*", end="")
        else:
            print(end=" ")
    print()
