import random
import time

quotesOfTheDay = {
    "Theodore Roosevelt" : "Believe you can and you're halfway there.",
    "Nelson Mandela" : "It always seems impossible until it's done.",
    "Unknown" : "Every day is a new beginning. Take a deep breath, smile, and start again.",
    "Vincent Van Gogh" : "Great things are done by a series of small things brought together.",
    "Aristotle" : "Happiness depends on ourselves.",
    "Buddha" : "No matter how hard the past is, you can always begin again.",
    "Mark Twain" : "The secret to getting ahead is to get started.",
    "Oscar Wilde" : "Be yourself; everyone else is already taken.",
    "Ralph Marston" : "What you do today can improve all your tomorrows.",
    "Eleanor Roosevelt" : "With the new day comes new strength and new thoughts."
}

messageForSadEmotion = "It's okay not to be okay. Feel all the feels. You got this."
messageForMadEmotion = "Whoa whoa whoa! Take a deep breath buddy! You don't need to react to everything that hurts you. Take a moment to calm your mind. You got this."
messageForOverwhelmedEmotion = "Pause for a moment. Take a deep breath. Relax. Take things one after another. And most of all, take it easy. You got this."
messageForAnxiousEmotion = "It's okay buddy. You don't need to solve everything at once. Take it easy, take a breath and slow down. Take things one after another. You got this."
messageForHappyEmotion = "Happiness looks good on you buddy! Celebrate all the little things you've accomplished and relish the moment. I'm happy for you."
messageForExcitedEmotion = "Feeling excited is a beautiful reminder that something great is happening for you. Take it all in and enjoy the moment. I'm happy for you."

#the different emotions in the list: Sad, Mad, Overwhelmed, Anxious (NEGATIVES) Happy, Excited (POSITIVES)
thingsToDoWhenPositive = [
    "go outside",
    "do something you really like",
    "relish the feeling",
    "spread your joy with others",
    "help other people have a good day",
    "journal your thoughts to remember the moment"
]

thingsToDoWhenNegative = [
    "slow down, take a deep breath",
    "try to talk to someone about how you're feeling",
    "journal your thoughts",
    "think about happy thoughts",
    "try to do something your really like to calm you down"
]

def threeSecCountdown():
    print("3")
    print()
    time.sleep(1)
    print("2")
    time.sleep(1)
    print()
    print("1")

def fiveSecCountdown():
    print("1")
    print() 
    time.sleep(1)
    print("2")
    print()
    time.sleep(1)
    print("3")
    print()
    time.sleep(1)
    print("4")
    print()
    time.sleep(1)
    print("5")
    print()

def breathingExcersizes():
    print("Let's start some breathing excerises!")
    quantityOfExcersize = int(input("How many times do you want to do this excersize? (1 excersize = 1 set of inhale/exhale) "))
    time.sleep(1)
    print("You chose to do this", quantityOfExcersize, "times.")
    time.sleep(1)
    print("Excersizes start in: ")
    threeSecCountdown()
    excersizesDone = 0
    while excersizesDone < quantityOfExcersize:
        print("Inhale for 5 seconds!")
        fiveSecCountdown()
        print("Exhale for 5 seconds!")
        fiveSecCountdown()
        excersizesDone += 1
    print("Task completed! Good job! Redirecting you to the main menu in 2 seconds!")
    time.sleep(2)
    welcomeInterface()

def portalToMainMenu():
    print("Thank you for doing this with me. Task completed.")
    time.sleep(1)
    print("redirecting you to the Main Menu in 2 seconds!")
    time.sleep(2)
    welcomeInterface()

def talkAboutFeelings():
    global howDoYouFeel
    howDoYouFeel = input("How do you feel today? Happy, Excited, Sad, Anxious, Overwhelmed, Mad? Your answer here: ")
    howDoYouFeel = howDoYouFeel.lower()
    if howDoYouFeel == "happy":
        print(messageForHappyEmotion)
        time.sleep(2)
        print()
        print("You should {} today!".format(random.choice(thingsToDoWhenPositive)))
        portalToMainMenu()
    elif howDoYouFeel == "excited":
        print(messageForExcitedEmotion)
        time.sleep(2)
        print()
        print("You should {} today!".format(random.choice(thingsToDoWhenPositive)))
        portalToMainMenu()
    elif howDoYouFeel == "sad":
        print(messageForSadEmotion)
        time.sleep(2)
        print()
        print("Oh well, to cheer you up, you should {} today!".format(random.choice(thingsToDoWhenNegative)))
        portalToMainMenu()
    elif howDoYouFeel == "anxious":
        print(messageForAnxiousEmotion)
        time.sleep(2)
        print()
        print("Oh well, to cheer you up, you should {} today!".format(random.choice(thingsToDoWhenNegative)))
        portalToMainMenu()
    elif howDoYouFeel == "overwhelmed":
        print(messageForOverwhelmedEmotion)
        time.sleep(2)
        print()
        print("Oh well, to cheer you up, you should {} today!".format(random.choice(thingsToDoWhenNegative)))
        portalToMainMenu()
    elif howDoYouFeel == "mad":
        print(messageForMadEmotion)
        time.sleep(2)
        print()
        print("Oh well, to cheer you up, you should {} today!".format(random.choice(thingsToDoWhenNegative)))
        portalToMainMenu()
    else:
        print("Oh. Sorry, we're limited to the emotions listed on the screen. Please put what you best feel like today, according to the options.")
        ElseElse = int(input("Or, did you want to do something else? Press 1 to retry, or 2 to return to the Main Menu"))
        if ElseElse == 1:
            print("Let's try this again.")
            time.sleep(0.5)
            talkAboutFeelings()
        elif ElseElse == 2:
            print("Returning you to the main menu in 2 seconds!")
            time.sleep(2)
            welcomeInterface()


def randomQuoteOfTheDay():
    number1 = quotesOfTheDay.keys()
    global figuresAsAList
    figuresAsAList = list(number1)
    randomFigure = random.choice(figuresAsAList)
    print("{} - {}".format(quotesOfTheDay.get(randomFigure), randomFigure))
    figuresAsAList.remove(randomFigure)

def quitCommand():
    print("Quitting command in 3 seconds. Thank you for visiting the M00d B00st3r v.1.0")
    time.sleep(3)
    print("goodbye! :)")

def quoteOfTheDay():
    print("You chose to hear a quote of the day!")
    time.sleep(0.5)
    print("Please select whom you want to hear the quote from, or you can choose a random quote!")
    time.sleep(0.5)
    print("Theodore Roosevelt, Nelson Mandela, Unknown, Vincent Van Gogh, Aristotle, Buddha, Mark Twain, Oscar Wilde, Ralph Marston, Eleanor Roosevelt")
    time.sleep(0.5)
    userSelection = input("Please enter their name or type 'random'")
    userSelection = userSelection.lower()
    if userSelection == "random":
        time.sleep(0.5)
        randomQuoteOfTheDay()
    elif userSelection == "theodore roosevelt":
        time.sleep(0.5)
        print("{} - Theodore Roosevelt".format(quotesOfTheDay.get("Theodore Roosevelt")))
    elif userSelection == "nelson mandela":
        time.sleep(0.5)
        print("{} - Nelson Mandela".format(quotesOfTheDay.get("Nelson Mandela")))
    elif userSelection == "unknown":
        time.sleep(0.5)
        print("{} - Unknown".format(quotesOfTheDay.get("Unknown")))
    elif userSelection == "vincent van gogh":
        time.sleep(0.5)
        print("{} - Vincent Van Gogh".format(quotesOfTheDay.get("Vincent Van Gogh")))
    elif userSelection == "aristotle":
        time.sleep(0.5)
        print("{} - Aristotle".format(quotesOfTheDay.get("Aristotle")))
    elif userSelection == "buddha":
        time.sleep(0.5)
        print("{} - Buddha".format(quotesOfTheDay.get("Buddha")))
    elif userSelection == "mark twain":
        time.sleep(0.5)
        print("{} - Mark Twain".format(quotesOfTheDay.get("Mark Twain")))
    elif userSelection == "oscar wilde":
        time.sleep(0.5)
        print("{} - Oscar Wilde".format(quotesOfTheDay.get("Oscar Wilde")))
    elif userSelection == "ralph marston":
        time.sleep(0.5)
        print("{} - Ralph Marston".format(quotesOfTheDay.get("Ralph Marston")))
    elif userSelection == "eleanor roosevelt":
        time.sleep(0.5)
        print("{} - Eleanor Roosevelt".format(quotesOfTheDay.get("Eleanor Roosevelt")))
    else:
        print("Maybe you spelled it wrong? Press 1 to review options again, 2 to return to Main Menu, 3 to QUIT")
        choice = int(input("Your answer here: "))
        if choice == 1:
            print("Revisiting options for Quotes of the Day in 2 seconds!")
            time.sleep(2)
            quoteOfTheDay()
        elif choice == 2:
            print("redirecting you to the Main Menu in 2 seconds!")
            time.sleep(2)
            welcomeInterface()
        else:
            quitCommand()
    choice2 = int(input("Press 1 to hear another quote of the day, press 2 to return to Main Menu"))
    if choice2 == 1:
        quoteOfTheDay()
    elif choice2 == 2:
        portalToMainMenu()
        

def welcomeInterface():
    print("Welcome to the Mood B00ster v1.0! What would you like to do today?")
    time.sleep(1)
    print("press 1 to talk about feelings, 2 to do a breathing excersize, 3 to get some quotes of the day, 4 to QUIT.")
    time.sleep(0.5)
    welcomeInput = int(input("Enter answer here: "))
    if welcomeInput == 1:
        talkAboutFeelings()
    elif welcomeInput == 2:
        print("Let's do some breathing excersizes!")
        time.sleep(0.5)
        print("Redirecting you there in 2 seconds!")
        time.sleep(2)
        breathingExcersizes()
    elif welcomeInput == 3:
        print("Okay, lets go hear a quote of the day to inspire you!")
        time.sleep(0.5)
        print("Redirecting you there in 2 seconds!")
        time.sleep(2)
        quoteOfTheDay()
    elif welcomeInput == 4:
        quitCommand()
    else:
        print("Please enter a valid option :)")
        time.sleep(0.5)
        print("Cycling back to the options in 1 second")
        time.sleep(1)
        welcomeInterface()


welcomeInterface()