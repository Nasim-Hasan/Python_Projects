import random

def main():
    print("Khansole Academy")
    i=0
    while i!=3:
        num1=random.randint(1,100)
        num2=random.randint(1,100)
        print("What is "+str(num1)+" + "+str(num2)+"?")
        answer=int(input("Your answer:"))
        if answer==num1+num2:
            print("Correct!")
            i=i+1
            print("You've gotten "+str(i)+" correct in a row.")
        else:
            print("Incorrect.")
            print("The expected answer is "+str(num1+num2))
            i=0
    
if __name__ == '__main__':
    main()