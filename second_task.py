fn = float(input("Enter first number: "))
sn = float(input("Enter second number: "))
tn = float(input("Enter third number: ")) # getting numbers

print(f"Max is {max(fn, sn, tn)}") # max with built-in function
# OR
if fn >= sn and fn >= tn:
    print(f"Max is {fn}")
elif sn >= fn and sn >= tn:
    print(f"Max is {sn}")
else:
    print(f"Max is {tn}") # max without built-in function
