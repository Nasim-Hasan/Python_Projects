import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
   for i in range (10):
        rand_num = random.randint (MIN_VALUE,MAX_VALUE)
        print(rand_num) 

if __name__ == '__main__':
    main()