
# Write your helper function here!

def main():
    num = int(input("Enter a number: "))
    # Call your helper function with `num` as a parameter!
    digit = num%10
    print("The ones digit is "+str(digit))
    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()