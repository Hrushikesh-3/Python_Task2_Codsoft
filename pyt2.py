def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print(" Add")
    print(" Subtract")
    print(" Multiply")
    print(" Divide")

    while True:
        choice = input("Enter choice (A/S/M/D): ")

        if choice in ('A', 'S', 'M', 'D'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == 'A':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == 'S':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == 'M':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == 'D':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

            next_calculation = input("Do you want to perform another calculation? (y/n): ")
            if next_calculation.lower() != 'y':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
