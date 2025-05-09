MAX_VALUE = 17

def main():
    for i in range(MAX_VALUE):
        j=i+1
        to_say = fizzbuzz(j)
        print(to_say)

def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "Fizzbuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return n

if __name__ == '__main__':
    main()