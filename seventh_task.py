a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: ")) # Getting sides from the user

if a + b > c and a + c > b and b + c > a: # Does this triangle even exist?
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b != c or a == c != b or b == c != a: # Checking all sides
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Такого треугольника не существует") # No, it's not
