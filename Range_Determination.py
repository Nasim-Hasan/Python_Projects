def in_range(n, low, high):
    if n>=low and n<=high:
        return True
    else:
        return False

# There is no need to edit code beyond this point

def main():
	n = int(input("n: "))
	low = int(input("low: "))
	high = int(input("high: "))
	if in_range(n, low, high):
		print("n is in range!")
	else:
		print("n is not in range...")


if __name__ == '__main__':
    main()