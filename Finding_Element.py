def find_karel(roster):
    """
    Prints "Karel isn't here." if 'karel' is not in the list `roster` and "Karel is here!" if 'karel' is present in `roster`.
    """
    if 'karel'in roster:
        print("Karel is here!")
    else:
        print("Karel isn't here.")

# There is no need to edit code beyond this point

def get_list():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list. All elements will be lowercase.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem.lower())
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    roster = get_list()
    find_karel(roster)

if __name__ == '__main__':
    main()