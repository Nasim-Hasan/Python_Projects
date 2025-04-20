def main():
    side1 = input("What is the length of side1?")
    side1 = float(side1)
    side2 = input("What is the length of side2?")
    side2 = float(side2)
    side3 = input("What is the length of side3?")
    side3 = float(side3)
    triangle_perimeter = side1+side2+side3
    print ("The perimeter of the triangle is "+str(triangle_perimeter))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()