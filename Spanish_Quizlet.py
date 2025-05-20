def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    correct=0
    for word in translations:
        spanish_word=input("What is the Spanish translation for "+word+"?")
        if spanish_word==translations[word]:
            print("That is correct!")
            correct+=1
        else:
            print("That is incorrect,"+" the Spanish translation for "+word+" is "+translations[word]+".")
        print()
    print("You got "+str(correct)+"/"+str(len(translations))+ " words correct,"+" come study again soon!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()