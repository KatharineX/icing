##You are tasked with writing a program that will read in a string and count the frequency of that number. 
##You only need to count the numbers in the range [0-9] inclusive.

numbers = str(input())
for i in range(0,10):
	string = str(numbers)
	x = string.count(str(i))
	i=i+1
	print("{}: {}".format(i-1, x))

