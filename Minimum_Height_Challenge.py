"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
MINIMUM_HEIGHT = 50 # arbitrary units :)

def main():
         # Ask the user for a height to check
    height = input("How tall are you? ")

    # If the user presses Enter immediately (without typing anything),
    # the result of input() will be an empty string (nothing between the quotation marks!)
    while height != "":
        height = float(height)  # Convert non-empty strings to be a float!
        
        # Perform height check
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

        # Ask the user for another height to check
        height = input("How tall are you? ")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()