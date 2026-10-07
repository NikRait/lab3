year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Check is enetered year leap
    print("Високосный год.")
else:
    print("Невисокосный год.")
