try:
    height = int(input("Enter your height in cm: "))
    age = int(input("Enter your age: "))
    bill = 0
except ValueError as e:
    print("Please enter a valid number")
    exit()

if height >= 120:
    print("You are allowed to ride the roller coaster.")

    if age < 12:
        print("The ticket price is $5 for children")
        bill += 5
    elif age < 18:
        print("The ticket price is $7 for teens")
        bill += 7
    elif 45 <= age <= 55:
        print("The ticket is free for our senior riders")
    else:
        print("The ticket cost $12 for adults.")
        bill += 12

    wants_photo = input("Do you want a photo for $3 (yes/no): ")
    if wants_photo.lower == 'yes' or 'y':
        print("Photo added to your bill.")
        bill += 3
        print(f"Your final bill is: {bill}")

else:
    print("You are not allowed to ride the roller coaster.")
