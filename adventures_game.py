print("Welcome to Treasure Island!\nYour mission is to find the treasure.")

left_right = str(input("You're at a crossroad. Where do you want to go? 'left' or 'right': ")).lower()

if left_right == 'left':

    swim_wait = str(input(
        "You've come across a lake, there is an island in the middle of the lake.\nDo you want to 'swim' or 'wait' for a boat? ")).lower()

    if swim_wait == "swim":
        print("Before reaching the island, you have no energy left and drown. Game Over")
    elif swim_wait == 'wait':
        print(
            "After waiting for a bit, a boat drift the the coast before you use it and go to the island in the middle of the lake.")
        left_right_door = str(input(
            "You've come across a house with three doors, the 'blue', the 'red' and the 'yellow' one. Which one are you choosing? ")).lower()
        if left_right_door == 'yellow':
            print("Congratulation! You found the treasure!")
        elif left_right_door ==


elif left_right == "right":
    print("You fall into a hole and dies. Game Over")
