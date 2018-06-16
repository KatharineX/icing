## Hearts 4 u
try:
    user_input = input("How much love you feeling? ")
    num = int(user_input)

    heart = '<3'
    empt = []
    for i in range(num):
        empt.append(heart)
        
    print("Enjoy!" + "".join(empt))

except:
  print("Sorry, try a number.")
