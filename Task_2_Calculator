def getdata():
    operand = int(input("\n Enter the Operand  : "))
    return operand


def addition(operands):
    return operands[0] + operands[1]


def subtraction(operands):
    return operands[0] - operands[1]


def multiplication(operands):
    return operands[0] * operands[1]


def division(operands):
    return operands[0] / operands[1]


def main():
    operands = []
    result = []
    answer = 0
    while True:
        print("===============================================")
        print("              SIMPLE CALCULATOR")
        print("===============================================")
        print("\n 1. Addition")
        print("\n 2. Subtraction")
        print("\n 3. Multiplication")
        print("\n 4. Division")
        print("\n 5. Exit")
        print("===============================================")
        operands.append(getdata())
        while True:
            choice = int(input("\n\n Enter the No. associated with the operation you want to perform : "))
            if choice == 1:
                operands.append(getdata())
                operands[0] = addition(operands)
                del operands[1]
                print("\n", operands)
            elif choice == 2:
                operands.append(getdata())
                operands[0] = subtraction(operands)
                del operands[1]
                print("\n", operands)
            elif choice == 3:
                operands.append(getdata())
                operands[0] = multiplication(operands)
                del operands[1]
                print("\n", operands)
            elif choice == 4:
                operands.append(getdata())
                operands[0] = division(operands)
                del operands[1]
                print("\n", operands)
            elif choice == 5:
                break
            else:
                print("Wrong Input")
        break

        print(operands)


main()
