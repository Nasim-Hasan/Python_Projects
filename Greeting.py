def main():
    name=input("What's your name?")
    print(greet(name))

# There is no need to edit code beyond this point

def greet(name):
	return "Greetings " + name + "!"
	
	
if __name__ == '__main__':
    main()