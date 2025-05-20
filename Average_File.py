def main():
    number_list = load_numbers_from_file("numbers.txt")
    # TODO: your code here
    sum=0
    for i in range (len(number_list)):
        sum=sum+number_list[i]
    
    avg=sum/len(number_list)
    print("Average: ",avg)

def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers

if __name__ == '__main__':
    main()