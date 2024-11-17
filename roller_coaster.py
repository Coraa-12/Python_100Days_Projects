from typing import Tuple, Optional

MIN_HEIGHT = 120 
CHILD_AGE_LIMIT = 12
TEEN_AGE_LIMIT = 18

TICKET_PRICES = {
    'child': 5,
    'teen': 7,
    'adult': 12
}

PHOTO_PRICE = 3

def get_validated_numeric_input(prompt: str, min_value: int = 0, max_value: int = 300) -> Optional[int]:
    """
    Get and validate numeric input from the user.
    
    Args:
        prompt: The input prompt to show to the user
        min_value: Minimum acceptable value
        max_value: Maximum acceptable value
    
    Returns:
        Optional[int]: The validated input value or None if invalid
    """
    try:
        value = int(input(prompt))
        if min_value <= value <= max_value:
            return value
        print(f"Please enter a value between {min_value} and {max_value}.")
        return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def get_yes_no_input(prompt: str) -> bool:
    """
    Get a yes/no response from the user.
    
    Args:
        prompt: The input prompt to show to the user
    
    Returns:
        bool: True for yes, False for no
    """
    while True:
        response = input(prompt).lower().strip()
        if response in ('yes', 'y'):
            return True
        if response in ('no', 'n'):
            return False
        print("Please answer 'yes' or 'no'.")

def calculate_ticket_price(age: int) -> int:
    """
    Calculate the base ticket price based on age.
    
    Args:
        age: The rider's age
    
    Returns:
        int: The ticket price
    """
    if age < CHILD_AGE_LIMIT:
        return TICKET_PRICES['child']
    elif age < TEEN_AGE_LIMIT:
        return TICKET_PRICES['teen']
    return TICKET_PRICES['adult']

def get_ticket_type(age: int) -> str:
    """
    Get the ticket type description based on age.
    
    Args:
        age: The rider's age
    
    Returns:
        str: The ticket type description
    """
    if age < CHILD_AGE_LIMIT:
        return "children"
    elif age < TEEN_AGE_LIMIT:
        return "teenagers"
    return "adults"

def process_rider() -> Tuple[bool, int]:
    """
    Process a single rider's information and calculate total bill.
    
    Returns:
        Tuple[bool, int]: (Success status, Total bill amount)
    """
    age = get_validated_numeric_input("Enter your age: ", 0, 120)
    if age is None:
        return False, 0

    height = get_validated_numeric_input("Enter your height in cm: ", 50, 250)
    if height is None:
        return False, 0

    if height < MIN_HEIGHT:
        print("Sorry, you are not tall enough to ride the roller coaster.")
        return True, 0

    ticket_type = get_ticket_type(age)
    bill = calculate_ticket_price(age)
    print(f"Ticket is ${bill} for {ticket_type}")

    if get_yes_no_input("Do you want a photo for $3? (yes/no): "):
        bill += PHOTO_PRICE

    return True, bill

def main():
    """Main function to run the roller coaster ticket system."""
    print("Welcome to the Roller Coaster!")
    
    success, bill = process_rider()
    
    if success and bill > 0:
        print(f"\nYour final bill is ${bill}")
        print("Enjoy your ride!")

if __name__ == "__main__":
    main()