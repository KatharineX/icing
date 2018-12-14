import sys
command_line = sys.argv[0:]

def balance():
	print('{} {}'.format(f_name, l_name))
	print('BSB: {}'.format(bsb))
	print('ACCNO: {}'.format(acc_no))
	print('BALANCE: {:.2f}'.format(bal)+'\n')
	
def deposit():
	global bal 
	fifties = int(input("How many 50's? "))
	twenties = int(input("How many 20's? "))
	tens = int((input("How many 10's? ")))
	fives= int((input("How many 5's? ")))
	new_total = float(fifties*50 + twenties*20 +tens*10+fives*5)

	if (fifties >=0) and (twenties >=0) and (tens >=0) and (fives >=0):
		bal = new_total + bal 
		print("SUCCESS: deposited {:.2f} into your account".format(new_total)+'\n')
	else:
		print("ERROR: Invalid input, specify a positive number")
	
def withdraw(money_amount):
	global bal 
	if money_amount > bal:
		print("ERROR: Unable to withdraw amount, amount requested is greater than balance."+'\n')
	elif money_amount < 0:
		print("ERROR: Unable to withdraw amount, amount requested is invalid")
	else:
		bal  = bal - money_amount
		print("SUCCESS: Withdrew {:.2f} from account".format(money_amount)+'\n')

def continuity():
	cont = input("Do you want to continue? Y/N ")
	if 'N' in cont:
		print("Have a nice day!")
		sys.exit()
	else: 
		next_action = input()
		if 'quit' in next_action:
			print("Have a nice day!")
		elif 'balance' in next_action:
			balance()
			continuity()
		elif 'withdraw' in next_action:
			money_amount = next_action.split()
			money_amount = float(money_amount[1])
			withdraw(money_amount)
			continuity()
		elif 'deposit' in next_action:
			deposit()
			continuity()
		else:
			pass

try:
	f_name = sys.argv[1]
	l_name = sys.argv[2]
	bsb = sys.argv[3]
	acc_no =sys.argv[4]
	bal = float(sys.argv[5])
	action = input()
	if 'balance' in action:
		balance()
		continuity()
	elif 'deposit' in action:
		deposit()
		continuity()
	elif 'withdraw' in action:
		withdraw()
		continuity()
	else:
		pass
	
except IndexError:
	print("ERROR: Not enough arguments supplied")
