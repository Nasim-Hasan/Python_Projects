MAX_LENGTH = 3

def shorten(lst):
    """
    Takes the provided list and removes elements from the end of the list--
    printing each removed element out--until the list has at most MAX_LENGTH
    elements inside of it.
    """
    if len(lst)==0:
        print("The list is empty")
    else:
        lstlength=len(lst)
        if lstlength>MAX_LENGTH:
            while lstlength>MAX_LENGTH:
                print(lst.pop())
                lstlength-=1
           

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()