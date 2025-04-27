def main():
    sequence_length = 0
    prev_num = float('-inf')  

    while True:
        num = float(input("Enter a non-decreasing number (or a smaller number to end the sequence): "))
        
        if num < prev_num:
            break

        sequence_length += 1
        prev_num = num

    print("The length of the sequence is:", sequence_length)



if __name__ == "__main__":
    main()