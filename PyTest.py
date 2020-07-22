weight = int(input("Enter Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() =="L":
    converted = weight*0.45
    print(f"You are {converted} Kilos")
elif unit.upper() =="K":
    converted = weight // 0.45
    print(f"You are {converted} pounds ")
else:
    print("please chose the correct option")