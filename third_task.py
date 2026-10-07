age = int(input("Enter how old are you: ")) # getting age from user

if age < 0:
    print("You cannot be this young") # secured fool
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
elif age <= 120:
    print("Old")
else:
    print("You cannot be this old") # another secured fool
