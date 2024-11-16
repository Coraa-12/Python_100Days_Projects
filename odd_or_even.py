try:
    number = int(input("Enter a number: "))
    is_number = "Even" if number % 2 == 0 else "Odd"
    print(f"The number of {number} is {is_number}")
except ValueError:
    print("Please enter a valid number.")