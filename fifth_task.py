string = input("Enter expression with spaces: ")
arr = string.split() # Splitting string from user
if len(arr) != 3:
    print("Wrong amount of characters")
else:
    fn = float(arr[0])
    sn = float(arr[2])

    match arr[1]:
        case "+":
            print(f"Result = {(fn + sn):.2f}")
        case "-":
            print(f"Result = {(fn - sn):.2f}")
        case "*":
            print(f"Result = {(fn * sn):.2f}")
        case "/":
            if sn == 0: # Checking division by zero
                print(f"In division second operand cannot be zero.")
            else:
                print(f"Result = {(fn / sn):.2f}")
        case _: # In the case that this operand does not exist
            print("There is no support for this operation")
