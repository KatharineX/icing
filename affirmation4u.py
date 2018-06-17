import time
##Daily Affirmations


user_input = input("Pop in a number between 1-9. See what the world has for you! " )
answer = int(user_input)

##Dramatic effects 
time.sleep(1)

affirmations = ["The world has squat for you. Enjoy the vestiges of your youth.", "Study for your exams! Crush it!",
"Baby, the stars are shining! Get a cup of coffee, listen to some sweet music and watch the stars tonight.", "You should definitely follow tsarstories on wordpress and tumblr :)",
"Read that book you've been putting off for ages.", "Smile! It looks good on you.", "You're gonna need a drink today.", "You! Are! Awesome!", "Don't cry because it's over. Smile because it happened."]

##An affirmation for you!
print("Your affirmation for the day is: {}".format(affirmations[answer-1]))

