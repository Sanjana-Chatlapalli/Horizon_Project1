import math

def display_menu():
    print("\n" + "="*50)
    print("        ADVANCED CALCULATOR")
    print("="*50)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm (log)")
    print("8. Trigonometry (sin, cos, tan)")
    print("9. Exit")
    print("="*50)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Enter a number.")

def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # EXIT
        if choice == '9':
            print("\n👋 Exiting Calculator... Thank you!")
            break

        # BASIC OPERATIONS
        elif choice in ['1','2','3','4','5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = num1 + num2
                print(f"✅ {num1} + {num2} = {result}")

            elif choice == '2':
                result = num1 - num2
                print(f"✅ {num1} - {num2} = {result}")

            elif choice == '3':
                result = num1 * num2
                print(f"✅ {num1} * {num2} = {result}")

            elif choice == '4':
                if num2 == 0:
                    print("❌ Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"✅ {num1} / {num2} = {result}")

            elif choice == '5':
                result = math.pow(num1, num2)
                print(f"✅ {num1}^{num2} = {result}")

        # SQUARE ROOT
        elif choice == '6':
            num = get_number("Enter number: ")
            if num < 0:
                print("❌ Cannot find square root of negative number!")
            else:
                print(f"✅ √{num} = {math.sqrt(num)}")

        # LOG
        elif choice == '7':
            num = get_number("Enter number: ")
            if num <= 0:
                print("❌ Log not defined for zero or negative!")
            else:
                print(f"✅ log({num}) = {math.log10(num)}")

        # TRIGONOMETRY
        elif choice == '8':
            angle = get_number("Enter angle in degrees: ")
            rad = math.radians(angle)

            print(f"\n--- Trigonometric Values ---")
            print(f"sin({angle}) = {math.sin(rad)}")
            print(f"cos({angle}) = {math.cos(rad)}")
            print(f"tan({angle}) = {math.tan(rad)}")

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    calculator()