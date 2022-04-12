weight = int(input("What's your weight? : "))

unit = input("(L)bs or (K)g ? : ")

if unit.upper() == "L":
    weight = weight * 0.45
    print(f'Your weight is {weight} Kg')

elif unit.upper() == "K":
    weight = weight / 0.45
    print(f'Your weight is {weight} Pounds')
