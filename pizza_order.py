def calculate_total(size: str, pepperoni: str, cheese: str) -> float:
    SIZE_PRICES = {
        'S': 15,
        'M': 20,
        'L': 25
    }

    size = size.upper()
    if size not in SIZE_PRICES:
        raise ValueError("Invalid size. Please choose from S, M, or L.")

    price = SIZE_PRICES[size]

    if pepperoni.upper() == 'Y':
        price += 2 if size == 'S' else 3

    if cheese.upper() == 'Y':
        price += 1

    return price

def get_valid_input(prompt: str, valid_options: set) -> str:
    while True:
        user_input = input(prompt)
        if user_input.upper() in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of {', '.join(valid_options)}")


def main():
    try:
        size = get_valid_input("Enter the size of the pizza (S, M, L): ", {'S', 'M', 'L'})
        pepperoni = get_valid_input("Do you want pepperoni? (Y, N): ", {'Y', 'N'})
        cheese = get_valid_input("Do you want extra cheese? (Y, N): ", {'Y', 'N'})

        total = calculate_total(size, pepperoni, cheese)
        print(f"Total price: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except KeyboardInterrupt:
        print("\nOrder cancelled.")
        return None

if __name__ == "__main__":
    main()
