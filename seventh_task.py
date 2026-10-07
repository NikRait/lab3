a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b != c or a == c != b or b == c != a:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Такого треугольника не существует")
