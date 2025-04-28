import random

def main():
    num_sides=int(input("How many sides does your dice have?"))
    roll=random.randint(1,num_sides)
    print("Your roll is "+str(roll))

if __name__ == '__main__':
    main()