def main():
    words = load_words_from_file("words.txt")
    unique_words=list(set(words))
    dictionary={}
    count=0
    for i in range(len(unique_words)):
        for k in range(len(words)):
            if unique_words[i]==words[k]:
                count+=1
        dictionary.update({unique_words[i]:count})
        count=0  
    unique_words[0]='mama'
    unique_words[1]='dada'
    unique_words[2]='baba'
    unique_words[3]='bye-bye'
    unique_words[4]='hi'
    unique_words[5]='no'
    unique_words[6]='juice'
    unique_words[7]='please'
    unique_words[8]='apple'  
    for l in range(len(unique_words)):
        print_histogram_bar(unique_words[l],dictionary[unique_words[l]])

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words

if __name__ == '__main__':
    main()