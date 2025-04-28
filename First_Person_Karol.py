N_COLS = 3
N_ROWS = 3

def main():
    print("Welcome to first person Karel! You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    
    # Set the starting direction and position of Karel
    facing_direction = 'East'  # This variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    curr_col = 1  # This variable ...
    curr_row = 1  # ... and this one keep track of Karel's position in the world! They may change if the user says to "move"
    
    # Get an action from the user
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    while action != '':  # If the user enters nothing for an action, exit the loop.
        # If the user wants to move forward and isn't blocked, update the relevant variables (row/col)
        if action == "move":
            if facing_direction == 'East' and curr_col < N_COLS:
                # Move right
                curr_col += 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            elif facing_direction == 'West' and curr_col > 1:
                # Move left
                curr_col -= 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            elif facing_direction == 'North' and curr_row < N_ROWS:
                # Move up
                curr_row += 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            elif facing_direction == 'South' and curr_row > 0:
                # Move down
                curr_row -= 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            else:
                print("You can't move forward!")

        # If the user wants Karel to turn, make Karel turn 90 degrees clockwise (updating the direction)
        elif action == "turn left":
            if facing_direction == 'East':
                facing_direction = 'North'
            elif facing_direction == 'North':
                facing_direction = 'West'
            elif facing_direction == 'West':
                facing_direction = 'South'
            elif facing_direction == 'South':
                facing_direction = 'East'
            print("You turned left and are now facing " + facing_direction + ".")

        # Ask for a new action to see if the user wants to continue
        action = input("What would you like to do? You can move and turn left. Press enter to finish. ")

    print("You've ended up at row " + str(curr_row) + " and column " + str(curr_col) + " facing " + facing_direction + ".")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()