
def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

def print_divisors(num):
    print ("Here are the divisors of "+str(num))
    for i in range (num):
        i+=1
        if(num%i==0):
            print(i)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()