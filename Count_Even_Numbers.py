def count_even(lst):
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
      lst.append(int(user_input))
      user_input = input("Enter an integer or press enter to stop: ") 
    even_count=0 
    for i in range(len(lst)):
       if(lst[i]%2==0):
           even_count+=1
    print(str(even_count))  

def main():
    lst=[]
    count_even(lst)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()