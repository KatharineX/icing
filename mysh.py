import os
import sys
import time

#### RECURSIVE FUNCTION TO USE IN CASE OF SITUATION WHERE COMMAND IS INITIATED ########
def PAM(command_line, command, arr_com, number, *words):
	try:
		arbritrary = 0
		variables = ["< ", " >", "|" ]
		# TESTING IF REDIRECTION OR PIPING IN THE CMD LINE
		for i in variables:
			if i in command_line:
				arbritrary = 1
				
		# ACCOUNTNG FOR REDIRECTION
		if arbritrary == 1:
			for i in variables:
				if " >" in i and i in command_line:
					new_comm_line = command_line.split(i)
					inputs = new_comm_line[0].strip()
					file = new_comm_line[1].strip()
					pid = os.fork()
					if pid == 0:
						our_file = open(file, "+w")
						our_file.write(inputs)
						our_file.close()
					else:
						os.wait()
						sys.exit()

				if i == "|" and i in command_line:
					new_comm_line = command_line.split(i)
					inputs2 = new_comm_line[0].strip()
					file2 = new_comm_line[1].strip()
					pid2 = os.fork()
					if pid2 == 0:
						our_file2 = open(file2, "+w")
						our_file2.write(inputs2)
						our_file2.close()
						show(file2)
					else:
						os.wait()
						sys.exit()

				if "< " in i and i in command_line:
					new_comm_line = command_line.split(i)
					file3 = new_comm_line[0].strip()
					inputs3 = new_comm_line[1].strip()
					if os.path.isfile(file3):
						s = open(file3, 'r')
						newss = s.read()
						s.close()
						if os.path.isfile(newss):
							show(newss)
						else:
							show(newss)
							sys.exit()
							
				else:
					pid3 = os.fork()
					if pid3 == 0:
						our_file3 = open(file3, "+w")
						our_file3.write(inputs3)
						our_file3.close()
						if file3 == "show":
							show(file3)
						else:
							os.wait()
							sys.exit()

				commands(number)
		
		### ENTERING THE FUNCTION AND TESTING FOR THE COMMAND ...
		if command_line == 'historylist':
			if number > 0:
				new_v_hist = v_hist[0:len(v_hist) -number]
			else:
				new_v_hist = v_hist
				
			if number == -1:
				for i in range(1):
					print(str(i)+": "+ new_v_hist[len(new_v_hist)-1])
					
			elif number == 0:
				for i in range(len(new_v_hist)):
					print(str(i)+": "+ new_v_hist[len(new_v_hist)-1-i])
						
			else:
				for i in range(len(new_v_hist)):
					print(str(i)+": "+ new_v_hist[len(new_v_hist)-1-i])

		elif command == 'exit':
			print("Goodbye!")
			sys.exit()
			
		####### IF COMMAND LINE IS LONGER THAN A SINGLE WORD, ACCOUNTING FOR THE SPECIFIC SITUATIONS #############
		elif len(arr_com) > 1:
			if arr_com[0] == 'unset':
				uvar = arr_com[1]
				phrase = uvar + "="
				if uvar in shell_dictionary:
					shell_dictionary.pop(uvar)	
			
			elif command == 'changedir':
				if len(arr_com) > 1:
					next_file = arr_com[1]
					history_list.append(next_file)
					v_hist.append("/".join(history_list))
					if '..' in next_file:
						del history_list[-1]
						del history_list[-1]
				
			elif 'say' == arr_com[0] or command == 'say' or command == 'echo':
				patek =[]
				for i in arr_com:
					if i[0] == "$":
						if i in shell_dictionary:
							print(shell_dictionary[i])

				if str(arr_com).count("$") > 0:
					for i in range(1,len(arr_com)):
						if arr_com[i][0] == "$":
							if arr_com[i][1:] in shell_dictionary:
								patek.append(shell_dictionary[arr_com[i][1:]])
							else:
								pass
						else:	
							patek.append(arr_com[i])
					print(" ".join(patek))

				if '\\' == command_line[len(command_line)-1]:
					words.append(command_line.replace("say ", ""))
					recursion(command_line, words, arr_com)

				if str(arr_com).count("$") == 0:
					print(*arr_com[1:])

			elif command == 'cdn':
				if len(arr_com) >= 2:
					numbs = int(arr_com[1])
					if numbs == 0:
						number = 0
					else:
						number += numbs
				if len(arr_com) == 1:
					number = 0
				
			elif command == 'show':
				try:
					comm_s = []
					if len(arr_com) > 1:
						for i in arr_com[1:]:
							comm_s.append(i)
					# ENTERING THE FUNCTION SHOW
					show(file, comm_s)
				except:
					pass

			elif command == 'set':
				if len(arr_com) == 1:
					for i, k in shell_dictionary.items():
						betted.append(i+"="+k)
					
					for i in sorted(betted[1:]):
						print(i)
					print("PS"+"="+shell_dictionary["PS"])

				elif len(arr_com) == 3:
					var = arr_com[1]
					sm = str(arr_com[2:]).replace("'","").replace("[","").replace("]","").replace(",","")
					
					if '$' in sm :
						shell_dictionary[var] = sm[1:]

					shell_dictionary[var] = sm
					setted.append(var+"="+sm)
						
					if var == 'PS':
						shell_dictionary["PS"] = sm
							
				elif len(arr_com) > 3:
					var = arr_com[1]
					sm = str(arr_com[2:]).replace("'","").replace("[","").replace("]","").replace(",","")
					
					if '$' in sm :
						shell_dictionary[var] = sm[1:]

					shell_dictionary[var] = sm
					setted.append(var+"="+sm)
					
					if var == 'PS':
						shell_dictionary["PS"] = sm
				else:
					pass
			
			elif command == 'sleep':
				zine = int(arr_com[1])
				time.sleep(zine)

		elif command == 'showdir' or command == "pwd":
			counter = 0
			try:
				if '/' in shell_dictionary['HOME']:
					counter = 1
					print(shell_dictionary['HOME'])
			except:
				pass
					
			if counter == 0:
				print("/".join(history_list))
				
		else:
			commands(number)

	except(EOFError):
		sys.exit()

## SHOW ACCOUNTS FOR THE INPUTS IN THE FILE , IT THEN READS 
## THE FILE AND ENTERS PAM TO ACT ACCORDINGLY TO THE INPUT.
def show(file, *files):
	############### OPTIONAL ACTION #####################
	for i in files:
		new_file = open(i, 'r')
		new_contents = new_file.read()
		new_file.close()
		new_split = new_contents.split(" ")
		PAM(new_contents, new_split[0], new_split, number)
	#####################################################
	
	comms = []
	score_file = open(file, 'r')
	contents = score_file.read()
	score_file.close()
	contents_arr = contents.split(" ")
	
	if os.path.exists(contents):
		n = open(contents, 'r')
		n_read = n.read()
		n_read_s = n_read.split(" ")
		n.close()
		PAM(n_read, n_read_s[0], n_read_s, number)
	else:
		PAM(contents, contents_arr[0], contents_arr, number)
	
## RECURSION() ACCOUNTS FOR THE LOOP IN THE CONTNUOUS LINES,
## IT READS THE CONTINUOUS LINES AND EDITS TO ATTAIN THE FINAL OUTPUT.
def recursion(command, words, arr_com):
	flipper =[]
	new = input("> ")
	list_new = new.split(" ")
	words.append(new)
	
	if new == "\\":
		recursion(command, words, arr_com)
	
	elif len(new) == 0:
		commands(number, command)
	
	try:
		if '\\' == new[len(new)-1] or 'say' in new:
			recursion(command, words, list_new)
	except:
		pass
	
	else:
		for i in words:
			if i == "\\":
				flipper.append(" ")
			else:
				try: 
					if "\\" == i[-1]:
						flipper.append(i[:-1])
					else:
						flipper.append(i)
				except:
					pass
					
		print("".join(flipper))
		commands(number, command)
		
## MAIN BODY OF COMMANDS, TRANSFORMING INPUT INTO PROMPTS/ ACTIONS.	
def commands(number, *command):
	try:
		################ INITIALISE ######################
		words = []
		arbritrary = 0
		variables = ["< ", " >", "|" ]
		betted = []
		########## INTO THE COMMAND #####################
		command_line = input(shell_dictionary["PS"]+" ")
		arr_com = command_line.split()
		
		if len(command_line) > 0:
			command = arr_com[0]
		else:
			command = ""
			commands(number)
			
		# TESTING IF REDIRECTION OR PIPING IN THE CMD LINE
		for i in variables:
			if i in command_line:
				arbritrary = 1
			
		# TEST FOR IF PATH NAME OF A FILE IN NAMESPACE
		if command_line.count('/') > 1:
			listicle = command_line.split(' ')
			command_to_do = command_line.split("/")
			future_command = command_to_do[len(command_to_do)-1]
			fut_command = command_to_do[len(command_to_do)-1].split(" ")
			if os.path.exists(listicle[0]) == 0:
				print("Unable to execute "+ command_line)
			else:
				if len(listicle) > 1:
					pid = os.fork();
					if pid == 0 :
						os.execv(listicle[0], listicle)
					else:
						os.wait()
				else:
					PAM(command_line, fut_command[0], command_to_do[len(command_to_do)-1].split(" "), number, words)
		
		if arbritrary == 1 or command_line[0].isalpha() == 1 or command_line[0] == '$' or command_line[0].isdigit() == 1 or command_line[0] == '/':
			try:
				if arr_com[0] in shell_dictionary:
					PAM(command_line, shell_dictionary[arr_com[0]], arr_com, number, words)
			except:
				pass
			# ACCOUNTING FOR REDIRECTION
			if arbritrary == 1:
				for i in variables:
					if " >" in i and i in command_line:
						new_comm_line = command_line.split(i)
						inputs = new_comm_line[0].strip()
						file = new_comm_line[1].strip()
						pid = os.fork()
						if pid == 0:
							our_file = open(file, "+w")
							our_file.write(inputs)
							our_file.close()
						else:
							os.wait()
							sys.exit()

					if i == "|" and i in command_line:
						new_comm_line = command_line.split(i)
						inputs2 = new_comm_line[0].strip()
						file2 = new_comm_line[1].strip()
						pid2 = os.fork()
						if pid2 == 0:
							our_file2 = open(file2, "+w")
							our_file2.write(inputs2)
							our_file2.close()
							show(file2)
						else:
							os.wait()
							sys.exit()

					if "< " in i and i in command_line:
						new_comm_line = command_line.split(i)
						file3 = new_comm_line[0].strip()
						inputs3 = new_comm_line[1].strip()
						if os.path.isfile(file3):
							s = open(file3, 'r')
							newss = s.read()
							s.close()
							if os.path.isfile(newss):
								show(newss)
							else:
								show(newss)
								sys.exit()
							
						else:
							pid3 = os.fork()
							if pid3 == 0:
								our_file3 = open(file3, "+w")
								our_file3.write(inputs3)
								our_file3.close()
								if file3 == "show":
									show(file3)
							else:
								os.wait()
								sys.exit()

				commands(number)

			if command_line == '\\':
				recursion(arr_com[0], words, arr_com)
				
			# TEST IF THE COMMAND IS IN THE SHELL_DICT & ACT IN ACCORDANCE
			if str(arr_com[0][1:]) in shell_dictionary:
				command = shell_dictionary[str(arr_com[0][1:])]
				PAM(command_line, command, arr_com, number )

			if command_line == 'historylist':
				if number > 0:
					new_v_hist = v_hist[0:len(v_hist) -number]
				else:
					new_v_hist = v_hist
				
				if number == -1:
					for i in range(1):
						print(str(i)+": "+ new_v_hist[len(new_v_hist)-1])
						
				elif number == 0:
					for i in range(len(new_v_hist)):
						print(str(i)+": "+ new_v_hist[len(new_v_hist)-1-i])
							
				else:
					for i in range(len(new_v_hist)):
						print(str(i)+": "+ new_v_hist[len(new_v_hist)-1-i])

			if command_line == 'exit':
				print("Goodbye!")
				sys.exit()

			if len(command) > 1:
				if arr_com[0] == 'unset':
					uvar = arr_com[1]
					phrase = uvar + "="
					if uvar in shell_dictionary:
						shell_dictionary.pop(uvar)
					
				elif arr_com[0] == 'changedir':
					if len(arr_com) > 1:
						next_file = arr_com[1]
						history_list.append(next_file)
						v_hist.append("/".join(history_list))
						if '..' in next_file:
							del history_list[-1]
							del history_list[-1]

				elif 'say' == arr_com[0]:
					patek =[]
					for i in arr_com:
						if i[0] == "$":
							if i in shell_dictionary:
								print(shell_dictionary[i])

					if str(arr_com).count("$") > 0:
						for i in range(1,len(arr_com)):
							if arr_com[i][0] == "$":
								if arr_com[i][1:] in shell_dictionary:
									patek.append(shell_dictionary[arr_com[i][1:]])
								else:
									pass
							else:	
								patek.append(arr_com[i])

						print(" ".join(patek))

					if '\\' == command_line[len(command_line)-1]:
						words.append(command_line.replace("say ", ""))
						recursion(command_line, words, arr_com)

					if str(arr_com).count("$") == 0:
						print(*arr_com[1:])

				elif arr_com[0] == 'cdn':
					#number = 0
					if len(arr_com) >= 2:
						numbs = int(arr_com[1])
						if numbs == 0:
							number = 0
						else:
							number += numbs
					if len(arr_com) == 1:
						number = 0

				elif arr_com[0] == 'show':
					try:
						if len(arr_com) > 1:
							for i in arr_com[1:]:
								show(i)
						else:
							show(file)
					except:
						pass
						
				elif arr_com[0] == 'set':
					
					if len(arr_com) == 1:
						for i, k in shell_dictionary.items():
							betted.append(i+"="+k)
						
						for i in sorted(betted[1:]):
							print(i)
						print("PS"+"="+shell_dictionary["PS"])

					elif len(arr_com) == 3:
						var = arr_com[1]
						sm = str(arr_com[2:]).replace("'","").replace("[","").replace("]","").replace(",","")
					
						if '$' in sm :
							shell_dictionary[var] = sm[1:]

						shell_dictionary[var] = sm
						setted.append(var+"="+sm)
						
						if var == 'PS':
							shell_dictionary["PS"] = sm
							
					elif len(arr_com) > 3:
						var = arr_com[1]
						sm = str(arr_com[2:]).replace("'","").replace("[","").replace("]","").replace(",","")
					
						if '$' in sm :
							shell_dictionary[var] = sm[1:]

						shell_dictionary[var] = sm
						setted.append(var+"="+sm)
						
						if var == 'PS':
							shell_dictionary["PS"] = sm
					else:
						pass

				elif arr_com[0] == 'sleep':
					zine = int(arr_com[1])
					time.sleep(zine)

			if command == 'showdir':
				counter = 0
				try:
					if '/' in shell_dictionary['HOME']:
						counter = 1
						print(shell_dictionary['HOME'])
				except:
					pass
					
					if counter == 0:
						print("/".join(history_list))
			else:
				commands(number)	
		
		commands(number)
	
	except(EOFError):
		sys.exit()

########################## MAIN ###############################
# VARIABLES ARE SET, COMMAND LINE ETC. ESTABLISHED 
setted = []
commandline = sys.argv[0:]
shell_dictionary = {'PS':'$'}
number = 0
history_list = []
wdir = os.getcwd()
history_list.append(wdir)
v_hist = []
v_hist.append(wdir)
new_v_hist = v_hist[:len(v_hist)-number]

################## INVOKING SHELL ############################
if len(commandline) == 1:
	commands(number)

elif len(commandline) == 2:
	# READING THE FILE AND INTERPRETING THE DATA WITH ASSUMPTION FORMATTING IS THE SAME AS REDIRECTION...
	optional_file = commandline[2]
	file = open(optional_file, 'r')
	contents = file.read().splitlines()
	file.close()
	file_stuff = contents.split(" ")
	PAM(file, file_stuff[0], file_stuff, number)
	
else:
	pass
