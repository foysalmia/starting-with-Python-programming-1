data = input("Enter input ")
while data != "Quit":
    value = int(data)
    if value == 0:
        print(f"{data} is Zero")
        data = input("Enter input ")
    elif value < 0:
        print(f"{data} is Negative")
        data = input("Enter input ")
    else:
        print(f"{data} is Positive")
        data = input("Enter input ")
