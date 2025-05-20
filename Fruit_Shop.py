def main():
    # fruits is a dictionary with keys being fruit names and values being the price of the corresponding fruit
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    price=0
    for name in fruits:
        number=int(input("How many ("+name+") do you want to buy?:")) 
        price=price+number*fruits[name]
    
    print("Your total is $"+str(price))

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()