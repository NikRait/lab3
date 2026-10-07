import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Cannot calculate")
else:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = ((-b - math.sqrt(d)) / 2*a)
        x2 = ((-b + math.sqrt(d)) / 2*a)
        print(f"First root = {x1:.2f}, second root = {x2:.2f}")
    elif d == 0:
        x1 = (-b/2*a)
        print(f"Root = {x1:.2f}")
    else:
        print("This expression has no roots")
