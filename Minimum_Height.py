"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
MINIMUM_HEIGHT = 50 # arbitrary units :)

def main():
        height = float(input("How tall are you? "))
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()