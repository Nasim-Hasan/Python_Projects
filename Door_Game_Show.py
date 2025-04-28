"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

def main():
    door = int(input("Door: "))  # Get user input for a door number
    
    while door < 1 or door > 3 :  # While the input is invalid 
       print("Invalid door!")  # Tell the user the input was invalid
       door = int(input("Door: "))  # Ask the user for a new input
    
    # Make an initial prize, we'll update it later based on which door is chosen!
    prize = 4
    
    # Pick a prize based on the door number
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        locked = prize % 2 != 0  # If prize isn't an even number, the door is locked
        if not locked:
            prize += 6
    elif door == 3 :
        for i in range(door):
            prize += i

    print("You win", prize, "prizes")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()