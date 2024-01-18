import random
import string


def SimplePass(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    collect = lower + upper + digits + symbols
    GeneratePass(collect, length)


def CustomizedPass(length):
    countAlpha = int(input("How many Alphabets you want in your password ?\n if want any from all then enter 52 :"))
    countSymbols = int(input("How many symbols you want in your password ?\n if want any from all then enter 32 :"))
    countDigits = int(input("How many Digits you want in your password ?\n if want any from all then enter 10 :"))
    alpha = ""
    symbols = ""
    digits = ""
    if length == countAlpha + countSymbols + countDigits or countAlpha == 52 or countSymbols == 32 or countDigits == 10:

        if countAlpha == len(string.ascii_letters):
            alpha = string.ascii_letters
        elif countAlpha <= length:
            print(" Enter the required Alphabets :")
            for i in range(countAlpha):
                while True :
                    print("Alphabet ", i + 1)
                    alphabet = input()
                    if alphabet[0].isalpha():
                        alpha = alpha + alphabet[0]
                        break
                    else:
                        print("This is not an alphabet...")

        if countSymbols == len(string.punctuation):
            symbols = string.punctuation
        elif countSymbols <= length:
            print(" Enter the required Symbols :")
            for i in range(countSymbols):
                while True:
                    print("Symbol ", i + 1)
                    symbol = input()
                    if symbol[0] in string.punctuation:
                        symbols = symbols + symbol[0]
                        break
                    else:
                        print("This is not a Special Symbol..")
        else:
            print("\n Password having only Symbols may be less secure")

        if countDigits == len(string.digits):
            digits = string.digits
        elif countDigits <= length:
            print(" Enter the required Digits :")
            for i in range(countDigits):
                while True:
                    print("Digit ", i + 1)
                    digit = input()
                    if digit[0] in string.digits:
                        digits = digits + digit[0]
                        break
                    else:
                        print("This is not a Digit...")
        else:
            print("\n Password having only Digits may be less secure")
    else:
        print("Invalid Inputs\n\n")
        CustomizedPass(length)
    collections = alpha + digits + symbols
    print("Generating password sequence from given data..")
    GeneratePass(collections, length)
    while True:
        ch = int(input("Want another password ? \n Enter 1 for YES : "))
        if ch == 1:
            GeneratePass(collections, length)
        else:
            return


def GeneratePass(collection, length):
    password = "".join(random.sample(collection, length))
    print("Your new password is : ", password)


def main():

    print("===============================================")
    print("              PASSWORD GENERATOR")
    print("===============================================")
    print("\n 1. Simple Password")
    print("\n 2. Customized Password")
    print("\n 3. Exit")
    print("===============================================")

    while True:
        choice = int(input("\n\nEnter the No. associated with the operation you want to perform : "))
        if choice == 1:
            length = int(input("Enter the length of the password:"))
            SimplePass(length)
        elif choice == 2:
            length = int(input("Enter the length of the password:"))
            CustomizedPass(length)
        elif choice == 3:
            break
        else:
            print("Wrong Input")


main()
