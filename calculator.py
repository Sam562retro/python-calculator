while True:
    print("Calculator commands: ")
    print("Press M to multiply")
    print("Press D to divide")
    print("Press A to add")
    print("Press S to subtract")
    print("Press Z to get final equal")
    print("Press Q to quit")

    while True:
        while True:
            try:
                n = int(input("enter number: "))
                break
            except:
                print("please enter a valid number")
