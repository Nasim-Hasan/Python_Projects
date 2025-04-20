def main():
    temp_co_officient = 5.0/9.0
    degrees_fahrenheit = input("Enter temperature in Fahrenheit:")
    degrees_fahrenheit = float(degrees_fahrenheit)
    degrees_celsius = (degrees_fahrenheit-32)*temp_co_officient
    print("Temperature: "+str(degrees_fahrenheit)+"F = "+str(degrees_celsius)+"C")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()