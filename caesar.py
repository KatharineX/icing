##Basic Caesar's Cipher. Could definitely be refined. And shortened. 

import sys

number = int(input("Enter key: "))

if number <0:
	print("Invalid key!")
	sys.exit()
else:
	line = str(input("Enter line: ")).strip(' ')
	new_line = list(line)
	
	alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7,  'i':8, 'j':9, 
				'k':10,'l':11, 'm':12, 'n':13, 'o':14,'p':15, 'q':16, 'r':17,  's':18, 
				't':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
	alpha_2 = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 
				10:'k',11:'l', 12:'m', 13:'n', 14:'o',15:'p', 16:'q', 17:'r',  18:'s', 
				19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
	list_for_val = []
	for i in range(0, len(line)):
		if line[i] in alphabet:
			list_for_val.append(alphabet[line[i]]+number)
		
	for l in range(0, len(list_for_val)):
		if list_for_val[l] > 25:
			list_for_val[l] = list_for_val[l] - 26
	quote = []
	for s in range(0, len(list_for_val)):
		if list_for_val[s] in alpha_2:
			quote.append(alpha_2[list_for_val[s]])
	
	final = ''.join(quote)
	print(final)
