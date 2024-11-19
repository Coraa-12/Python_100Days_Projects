print("Welcome to Treasure Island!\nYour mission is to find the treasure.")

left_right = str(input("You're at a crossroad. Where do you want to go? 'left' or 'right': ")).lower()

if left_right == 'left':

    swim_wait = str(input("You've come across a lake, there is an island in the middle of the lake.\nDo you want to 'swim' or 'wait' for a boat? ")).lower()
    
elif left_right