string = input("Enter expression with spaces: ")
arr = string.split()
if len(arr) != 3:
    print("Wrong amount of operands")
else:
    fn = float(arr[0])
    sn = float(arr[2])

    match arr[1]:
        case "+":
            print(f"Result = {fn + sn}")
        case "-":
            print(f"Result = {fn - sn}")
        case "*":
            print(f"Result = {(fn * sn):.2f}")
        case "/":
            if sn == 0:
                print(f"In division second number cannot be zero.")
            else:
                print(f"Result = {(fn / sn):.2f}")
        case _:
            print("There is no support for this operand")
