def main():
    string=input("Enter a String:")
    reverse_string=string[::-1]
    if reverse_string==string:
        print("String is Palindrome.")
    else:
        print("String is not Palindrome.")

if __name__ == "__main__":
    main()