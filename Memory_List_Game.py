import random

NUM_PAIRS = 3

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    index=0
    truth_list=[]
    displayed_list=[]
    for i in range(2*NUM_PAIRS):
        if i<NUM_PAIRS:
            truth_list.append(i)
        else:
            truth_list.append(index)
            index+=1
        displayed_list.append('*')
    random.shuffle(truth_list)
    
    while True:
        if '*' not in displayed_list:
            break
        else:
            print(displayed_list)
            a=int(input("Enter an index:"))
            if a<0 or a>2*NUM_PAIRS-1:
                while a<0 or a>2*NUM_PAIRS-1:
                    print("Invalid index")
                    a=int(input("Enter an index again:"))
            b=int(input("Enter an index:"))
            if b<0 or b>2*NUM_PAIRS-1:
                while b<0 or b>2*NUM_PAIRS-1:
                    print("Invalid index")
                    b=int(input("Enter an index again:"))
            if truth_list[a]==truth_list[b]:
                print("Match!")
                displayed_list[a]=truth_list[a]
                displayed_list[b]=truth_list[b]
            else:
                print("Value at index ",a," is",truth_list[a])
                print("Value at index ",b," is",truth_list[b])
                print("No match. Try again!")
        clear_terminal()     
    print(displayed_list)
    print("You Won")

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()