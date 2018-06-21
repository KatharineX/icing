import time
##Daily Affirmations


user_input = input("Pop in a number between 1-11. See what the world has for you! " )
answer = int(user_input)

##Dramatic effects 
time.sleep(1)

affirmations = ["The world has squat for you. Enjoy the vestiges of your youth.", "Study for your exams! Crush it!", "Try matcha! It has the benefits of caffiene without the negative side effects.",
"Baby, the stars are shining! Get a cup of coffee, listen to some sweet music and watch the stars tonight.", "FEEL GOOD ABOUT UR DECISIONS. EVERYTHING HAS ITS REASON AND RHYME.",
"Read that book you've been putting off for ages.", "Smile! It looks good on you.", "You're gonna need a drink today.", "You! Are! Awesome!", "Don't cry because it's over. Smile because it happened.", 
               "Sometimes, giving up is the right thing."]

##An affirmation for you!
print("Your affirmation for the day is: {}".format(affirmations[answer-1]))

